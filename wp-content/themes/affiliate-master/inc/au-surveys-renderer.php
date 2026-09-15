<?php
/**
 * AU Surveys presentation renderer.
 *
 * Pure presentation only: callers must supply the governed read model.
 * This file must not load canonical/staging data, resolve affiliate URLs,
 * or infer publisher approval.
 */

declare(strict_types=1);

function affiliate_master_escape_text(mixed $value): string
{
    return htmlspecialchars((string) $value, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
}

function affiliate_master_render_au_surveys_list(array $records): string
{
    $safe = array_values(array_filter($records, static function (array $record): bool {
        return ($record['display_state'] ?? null) === 'INFORMATIONAL_VERIFIED';
    }));

    usort($safe, static function (array $a, array $b): int {
        return ((int) ($a['rank'] ?? PHP_INT_MAX)) <=> ((int) ($b['rank'] ?? PHP_INT_MAX));
    });

    if ($safe === []) {
        return '<p class="affiliate-surveys-empty">No currently verified survey programs are available for comparison.</p>';
    }

    $html = '<div class="affiliate-surveys-list" data-commercial-state="blocked">';
    foreach ($safe as $record) {
        $commercialState = (string) ($record['commercial_state'] ?? 'BLOCKED');
        $html .= '<article class="affiliate-survey-card">';
        $html .= '<h3>' . affiliate_master_escape_text($record['name'] ?? '') . '</h3>';
        $html .= '<p class="affiliate-survey-tier">' . affiliate_master_escape_text($record['tier'] ?? '') . '</p>';
        $html .= '<p>' . affiliate_master_escape_text($record['participation_summary'] ?? '') . '</p>';
        $html .= '<p><strong>Rewards:</strong> ' . affiliate_master_escape_text($record['reward_summary'] ?? '') . '</p>';
        $html .= '<p><strong>Evidence:</strong> ' . affiliate_master_escape_text($record['freshness_state'] ?? '')
            . ' · verified ' . affiliate_master_escape_text($record['last_verified_at'] ?? '') . '</p>';
        $html .= '<p><strong>Commercial status:</strong> ' . affiliate_master_escape_text($commercialState) . '</p>';
        if ($commercialState === 'BLOCKED' || empty($record['commercial_action'])) {
            $html .= '<p class="affiliate-survey-commercial-note">Informational only — no commercial destination is enabled.</p>';
        }
        $html .= '</article>';
    }
    $html .= '</div>';

    return $html;
}

function affiliate_master_render_au_survey_detail(array $record): string
{
    if (($record['display_state'] ?? null) !== 'INFORMATIONAL_VERIFIED') {
        return '<p class="affiliate-survey-unavailable">This program is still under research and is not ready for publication.</p>';
    }

    $commercialState = (string) ($record['commercial_state'] ?? 'BLOCKED');
    $html = '<section class="affiliate-survey-detail" data-commercial-state="' . affiliate_master_escape_text(strtolower($commercialState)) . '">';
    $html .= '<h2>' . affiliate_master_escape_text($record['name'] ?? '') . '</h2>';
    $html .= '<p>' . affiliate_master_escape_text($record['participation_summary'] ?? '') . '</p>';
    $html .= '<p><strong>Rewards:</strong> ' . affiliate_master_escape_text($record['reward_summary'] ?? '') . '</p>';
    $html .= '<dl>';
    $html .= '<dt>Evidence state</dt><dd>' . affiliate_master_escape_text($record['evidence_state'] ?? '') . '</dd>';
    $html .= '<dt>Freshness</dt><dd>' . affiliate_master_escape_text($record['freshness_state'] ?? '') . '</dd>';
    $html .= '<dt>Last verified</dt><dd>' . affiliate_master_escape_text($record['last_verified_at'] ?? '') . '</dd>';
    $html .= '<dt>Review due</dt><dd>' . affiliate_master_escape_text($record['review_due_at'] ?? '') . '</dd>';
    $html .= '</dl>';

    if ($commercialState === 'BLOCKED' || empty($record['commercial_action'])) {
        $html .= '<p class="affiliate-survey-commercial-note">Commercial action blocked pending governed publisher and destination approval.</p>';
    }

    $html .= '</section>';
    return $html;
}
