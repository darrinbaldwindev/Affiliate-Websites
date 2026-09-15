<?php

declare(strict_types=1);

$root = dirname(__DIR__, 2);
require_once $root . '/wp-content/themes/affiliate-master/inc/au-surveys-renderer.php';

$input = $argv[1] ?? '';
if ($input === '' || ! is_file($input)) {
    fwrite(STDERR, "Expected presentation read-model JSON path.\n");
    exit(2);
}

$data = json_decode((string) file_get_contents($input), true, 512, JSON_THROW_ON_ERROR);
$records = $data['records'] ?? [];

function expect_true(bool $condition, string $message): void
{
    if (! $condition) {
        fwrite(STDERR, "FAIL: {$message}\n");
        exit(1);
    }
}

$listHtml = affiliate_master_render_au_surveys_list($records);
expect_true(str_contains($listHtml, 'Octopus Group'), 'verified flagship should render');
expect_true(str_contains($listHtml, 'Pureprofile'), 'second verified flagship should render');
expect_true(! str_contains($listHtml, 'YouGov'), 'research-hold record must not render in verified list');
expect_true(! str_contains($listHtml, '<a '), 'renderer must not emit links while commercial action is blocked');
expect_true(! str_contains($listHtml, 'http://') && ! str_contains($listHtml, 'https://'), 'renderer must not leak URLs');
expect_true(substr_count($listHtml, 'Informational only — no commercial destination is enabled.') >= 1, 'blocked commercial state must be visible');

$octopus = null;
foreach ($records as $record) {
    if (($record['id'] ?? null) === 'octopus-group-au') {
        $octopus = $record;
        break;
    }
}
expect_true(is_array($octopus), 'octopus detail fixture must exist');
$detailHtml = affiliate_master_render_au_survey_detail($octopus);
expect_true(str_contains($detailHtml, 'Octopus Group'), 'detail must use same governed identity');
expect_true(str_contains($detailHtml, 'Commercial action blocked'), 'detail must expose blocked action state');
expect_true(! str_contains($detailHtml, '<a '), 'detail must not emit an affiliate link while blocked');

$malicious = $octopus;
$malicious['name'] = '<script>alert(1)</script>';
$escaped = affiliate_master_render_au_survey_detail($malicious);
expect_true(! str_contains($escaped, '<script>'), 'renderer must escape untrusted text');
expect_true(str_contains($escaped, '&lt;script&gt;alert(1)&lt;/script&gt;'), 'escaped malicious text should remain visible as text');

$research = [
    'display_state' => 'RESEARCH_REQUIRED',
    'name' => 'Research Hold',
    'commercial_state' => 'BLOCKED',
    'commercial_action' => null,
];
$researchHtml = affiliate_master_render_au_survey_detail($research);
expect_true(str_contains($researchHtml, 'still under research'), 'research-hold detail must fail closed');
expect_true(! str_contains($researchHtml, 'Research Hold'), 'research-hold detail must not expose draft program content');

$unsafeAction = $octopus;
$unsafeAction['commercial_state'] = 'BLOCKED';
$unsafeAction['commercial_action'] = ['url' => 'https://evil.example/track'];
$unsafeHtml = affiliate_master_render_au_survey_detail($unsafeAction);
expect_true(! str_contains($unsafeHtml, 'evil.example'), 'blocked state must ignore injected commercial action');
expect_true(! str_contains($unsafeHtml, '<a '), 'blocked state must never render injected action link');

fwrite(STDOUT, "AU surveys theme renderer verification passed for " . count($records) . " governed records.\n");
