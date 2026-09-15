<?php

declare(strict_types=1);

// Minimal WordPress contract harness. This executes the real theme bootstrap and
// shortcode callbacks without claiming a full WordPress/database/browser runtime.
define('ABSPATH', __DIR__ . '/');

$GLOBALS['affiliate_test_shortcodes'] = [];
$GLOBALS['affiliate_test_filters'] = [];

function get_theme_file_path(string $path = ''): string
{
    return dirname(__DIR__, 2) . '/wp-content/themes/affiliate-master/' . ltrim($path, '/');
}
function add_action(string $hook, callable $callback): void {}
function add_theme_support(string $feature): void {}
function add_editor_style(string $stylesheet): void {}
function wp_enqueue_style(...$args): void {}
function get_stylesheet_uri(): string { return 'style.css'; }
function wp_get_theme(): object { return new class { public function get(string $key): string { return '0.1.0'; } }; }
function add_shortcode(string $tag, callable $callback): void { $GLOBALS['affiliate_test_shortcodes'][$tag] = $callback; }
function apply_filters(string $tag, mixed $value): mixed
{
    return array_key_exists($tag, $GLOBALS['affiliate_test_filters'])
        ? $GLOBALS['affiliate_test_filters'][$tag]
        : $value;
}

require_once dirname(__DIR__, 2) . '/wp-content/themes/affiliate-master/functions.php';

function seam_expect(bool $condition, string $message): void
{
    if (! $condition) {
        fwrite(STDERR, "FAIL: {$message}\n");
        exit(1);
    }
}

seam_expect(isset($GLOBALS['affiliate_test_shortcodes']['affiliate_au_surveys_list']), 'list shortcode must register');
seam_expect(isset($GLOBALS['affiliate_test_shortcodes']['affiliate_au_survey_detail']), 'detail shortcode must register');

$list = $GLOBALS['affiliate_test_shortcodes']['affiliate_au_surveys_list'];
$detail = $GLOBALS['affiliate_test_shortcodes']['affiliate_au_survey_detail'];

// No governed provider: fail closed.
$emptyList = $list();
seam_expect(str_contains($emptyList, 'No currently verified survey programs'), 'list must fail closed without provider');
$emptyDetail = $detail();
seam_expect(str_contains($emptyDetail, 'not currently available for governed display'), 'detail must fail closed without provider/program identity');
seam_expect(! str_contains($emptyDetail, '<a '), 'empty detail must not emit link');

$record = [
    'id' => 'fixture-program-au',
    'name' => 'Fixture Program',
    'display_state' => 'INFORMATIONAL_VERIFIED',
    'tier' => 'FLAGSHIP',
    'rank' => 1,
    'participation_summary' => 'Fixture participation.',
    'reward_summary' => 'Fixture reward.',
    'evidence_state' => 'verified_primary',
    'freshness_state' => 'CURRENT',
    'last_verified_at' => '2026-09-15',
    'review_due_at' => '2026-10-15',
    'commercial_state' => 'BLOCKED',
    'commercial_action' => null,
];
$GLOBALS['affiliate_test_filters']['affiliate_master_au_surveys_read_model'] = [$record];
$GLOBALS['affiliate_test_filters']['affiliate_master_au_survey_program_id'] = 'fixture-program-au';

$renderedList = $list();
$renderedDetail = $detail();
seam_expect(str_contains($renderedList, 'Fixture Program'), 'governed provider record must reach list renderer');
seam_expect(str_contains($renderedDetail, 'Fixture Program'), 'same governed identity must reach detail renderer');
seam_expect(str_contains($renderedDetail, 'Commercial action blocked'), 'blocked state must survive WordPress seam');
seam_expect(! str_contains($renderedList . $renderedDetail, '<a '), 'blocked seam must not emit links');

// Unknown requested identity: fail closed instead of falling back to another record.
$GLOBALS['affiliate_test_filters']['affiliate_master_au_survey_program_id'] = 'missing-program-au';
$missing = $detail();
seam_expect(str_contains($missing, 'not currently available for governed display'), 'unknown identity must fail closed');
seam_expect(! str_contains($missing, 'Fixture Program'), 'unknown identity must not fall through to another record');

// Malformed provider output: fail closed.
$GLOBALS['affiliate_test_filters']['affiliate_master_au_surveys_read_model'] = 'not-an-array';
seam_expect(str_contains($list(), 'No currently verified survey programs'), 'malformed list provider must fail closed');
seam_expect(str_contains($detail(), 'not currently available for governed display'), 'malformed detail provider must fail closed');

fwrite(STDOUT, "AU surveys WordPress presentation seam verification passed.\n");
