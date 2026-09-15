<?php
/**
 * Affiliate Master — minimal theme bootstrap.
 */

declare(strict_types=1);

if (! defined('ABSPATH')) {
    exit;
}

require_once get_theme_file_path('inc/au-surveys-renderer.php');

add_action('after_setup_theme', static function (): void {
    add_theme_support('wp-block-styles');
    add_theme_support('responsive-embeds');
    add_theme_support('editor-styles');
    add_editor_style('style.css');
});

add_action('wp_enqueue_scripts', static function (): void {
    wp_enqueue_style(
        'affiliate-master-style',
        get_stylesheet_uri(),
        [],
        wp_get_theme()->get('Version')
    );
});

/**
 * Presentation-only seam. A governed plugin/API adapter may provide records
 * through the affiliate_master_au_surveys_read_model filter. The theme does
 * not load canonical/staging data itself.
 */
add_shortcode('affiliate_au_surveys_list', static function (): string {
    $records = apply_filters('affiliate_master_au_surveys_read_model', []);
    if (! is_array($records)) {
        $records = [];
    }

    return affiliate_master_render_au_surveys_list($records);
});

add_shortcode('affiliate_au_survey_detail', static function (): string {
    $records = apply_filters('affiliate_master_au_surveys_read_model', []);
    $programId = apply_filters('affiliate_master_au_survey_program_id', '');

    if (! is_array($records) || ! is_string($programId) || $programId === '') {
        return '<p class="affiliate-survey-unavailable">This survey program is not currently available for governed display.</p>';
    }

    foreach ($records as $record) {
        if (is_array($record) && ($record['id'] ?? null) === $programId) {
            return affiliate_master_render_au_survey_detail($record);
        }
    }

    return '<p class="affiliate-survey-unavailable">This survey program is not currently available for governed display.</p>';
});
