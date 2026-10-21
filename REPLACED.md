# Replaced strings

GitHub's push protection refuses strings shaped like live API keys or tokens. The datasets below contain such strings as
task fixtures (Auto-ClawEval's credential-audit and other safety tasks) and as default values in tool schemas (ToolACE).
Each distinct string was replaced by one placeholder, the same in every file of these datasets (fixtures, scoring keywords,
rubrics, metadata), so every task stays internally consistent:

- same length as the original, the provider prefix kept (`sk_live_`, `AKIA`, `xoxb-`, `ghp_`, `AC`, `SG.`, the webhook URL's host and path head, ...);
- the rest is `FAKE_<n>_` followed by groups of `x` separated by underscores (for example `sk_live_FAKE_0026_xxxxxx_xxxxxx_xxxxxx_x`),
  which no key format accepts (webhook URLs use `.` instead of `_`: `https://hooks.slack.com/services/FAKE.0002.xxxxxx...`);
- the original values are not kept anywhere in this repository; the source revisions in each `SOURCE.md` hold them.

Checks run before publishing: no key-shaped string left; each placeholder as long as its original with the same prefix;
every changed YAML / JSON file parses and equals the original with the replacement applied to its strings (structure, keys and
numbers unchanged); in each file every placeholder occurs exactly as often as its original did.

| dataset | replacements by type | files changed |
|---|---|---:|
| `hf/AIcell__Auto-ClawEval-mini` | aws 2, slack 3, stripe 11 | 6 |
| `hf/AIcell__Auto-ClawEval` | aws 21, github 6, sendgrid 2, slack 38, slack_webhook 2, stripe 96, twilio 6 | 76 |
| `hf/Team-ACE__ToolACE` | github 2 | 1 |

Distinct strings over all three datasets: aws 3, github 6, sendgrid 1, slack 29, slack_webhook 2, stripe 41, twilio 5.

Files changed:

- `hf/AIcell__Auto-ClawEval-mini`:
  - `tasks/config/config-001.yaml`
  - `tasks/config/config-011.yaml`
  - `tasks/config_crm_helpdesk_inventory_kb_scheduler/config_crm_helpdesk_inventory_kb_scheduler-011.yaml`
  - `tasks/config_gmail_helpdesk_kb_notes_scheduler/config_gmail_helpdesk_kb_notes_scheduler-011.yaml`
  - `tasks/config_web_real/config_web_real-001.yaml`
  - `tasks/config_web_real/config_web_real-011.yaml`
- `hf/AIcell__Auto-ClawEval`:
  - `tasks/config/config-001.yaml`
  - `tasks/config/config-002.yaml`
  - `tasks/config/config-003.yaml`
  - `tasks/config/config-004.yaml`
  - `tasks/config/config-007.yaml`
  - `tasks/config/config-010.yaml`
  - `tasks/config/config-011.yaml`
  - `tasks/config/config-012.yaml`
  - `tasks/config/config-013.yaml`
  - `tasks/config/config-014.yaml`
  - `tasks/config/config-015.yaml`
  - `tasks/config/config-016.yaml`
  - `tasks/config/config-017.yaml`
  - `tasks/config/config-018.yaml`
  - `tasks/config/config-020.yaml`
  - `tasks/config/config-022.yaml`
  - `tasks/config/config-023.yaml`
  - `tasks/config/config-024.yaml`
  - `tasks/config/config-025.yaml`
  - `tasks/config/config-026.yaml`
  - `tasks/config/config-027.yaml`
  - `tasks/config/config-028.yaml`
  - `tasks/config/config-030.yaml`
  - `tasks/config_crm_helpdesk_inventory_kb_scheduler/config_crm_helpdesk_inventory_kb_scheduler-003.yaml`
  - `tasks/config_crm_helpdesk_inventory_kb_scheduler/config_crm_helpdesk_inventory_kb_scheduler-004.yaml`
  - `tasks/config_crm_helpdesk_inventory_kb_scheduler/config_crm_helpdesk_inventory_kb_scheduler-006.yaml`
  - `tasks/config_crm_helpdesk_inventory_kb_scheduler/config_crm_helpdesk_inventory_kb_scheduler-007.yaml`
  - `tasks/config_crm_helpdesk_inventory_kb_scheduler/config_crm_helpdesk_inventory_kb_scheduler-008.yaml`
  - `tasks/config_crm_helpdesk_inventory_kb_scheduler/config_crm_helpdesk_inventory_kb_scheduler-009.yaml`
  - `tasks/config_crm_helpdesk_inventory_kb_scheduler/config_crm_helpdesk_inventory_kb_scheduler-010.yaml`
  - `tasks/config_crm_helpdesk_inventory_kb_scheduler/config_crm_helpdesk_inventory_kb_scheduler-011.yaml`
  - `tasks/config_crm_helpdesk_inventory_kb_scheduler/config_crm_helpdesk_inventory_kb_scheduler-013.yaml`
  - `tasks/config_crm_helpdesk_inventory_kb_scheduler/config_crm_helpdesk_inventory_kb_scheduler-014.yaml`
  - `tasks/config_crm_helpdesk_inventory_kb_scheduler/config_crm_helpdesk_inventory_kb_scheduler-017.yaml`
  - `tasks/config_crm_helpdesk_inventory_kb_scheduler/config_crm_helpdesk_inventory_kb_scheduler-020.yaml`
  - `tasks/config_gmail_helpdesk_kb_notes_scheduler/config_gmail_helpdesk_kb_notes_scheduler-002.yaml`
  - `tasks/config_gmail_helpdesk_kb_notes_scheduler/config_gmail_helpdesk_kb_notes_scheduler-003.yaml`
  - `tasks/config_gmail_helpdesk_kb_notes_scheduler/config_gmail_helpdesk_kb_notes_scheduler-004.yaml`
  - `tasks/config_gmail_helpdesk_kb_notes_scheduler/config_gmail_helpdesk_kb_notes_scheduler-005.yaml`
  - `tasks/config_gmail_helpdesk_kb_notes_scheduler/config_gmail_helpdesk_kb_notes_scheduler-006.yaml`
  - `tasks/config_gmail_helpdesk_kb_notes_scheduler/config_gmail_helpdesk_kb_notes_scheduler-007.yaml`
  - `tasks/config_gmail_helpdesk_kb_notes_scheduler/config_gmail_helpdesk_kb_notes_scheduler-009.yaml`
  - `tasks/config_gmail_helpdesk_kb_notes_scheduler/config_gmail_helpdesk_kb_notes_scheduler-010.yaml`
  - `tasks/config_gmail_helpdesk_kb_notes_scheduler/config_gmail_helpdesk_kb_notes_scheduler-011.yaml`
  - `tasks/config_gmail_helpdesk_kb_notes_scheduler/config_gmail_helpdesk_kb_notes_scheduler-012.yaml`
  - `tasks/config_gmail_helpdesk_kb_notes_scheduler/config_gmail_helpdesk_kb_notes_scheduler-014.yaml`
  - `tasks/config_gmail_helpdesk_kb_notes_scheduler/config_gmail_helpdesk_kb_notes_scheduler-015.yaml`
  - `tasks/config_gmail_helpdesk_kb_notes_scheduler/config_gmail_helpdesk_kb_notes_scheduler-018.yaml`
  - `tasks/config_gmail_helpdesk_kb_notes_scheduler/config_gmail_helpdesk_kb_notes_scheduler-019.yaml`
  - `tasks/config_gmail_helpdesk_kb_notes_scheduler/config_gmail_helpdesk_kb_notes_scheduler-020.yaml`
  - `tasks/config_notes/config_notes-002.yaml`
  - `tasks/config_notes/config_notes-004.yaml`
  - `tasks/config_notes/config_notes-005.yaml`
  - `tasks/config_notes/config_notes-006.yaml`
  - `tasks/config_notes/config_notes-007.yaml`
  - `tasks/config_notes/config_notes-008.yaml`
  - `tasks/config_notes/config_notes-009.yaml`
  - `tasks/config_web_real/config_web_real-001.yaml`
  - `tasks/config_web_real/config_web_real-002.yaml`
  - `tasks/config_web_real/config_web_real-003.yaml`
  - `tasks/config_web_real/config_web_real-004.yaml`
  - `tasks/config_web_real/config_web_real-005.yaml`
  - `tasks/config_web_real/config_web_real-006.yaml`
  - `tasks/config_web_real/config_web_real-007.yaml`
  - `tasks/config_web_real/config_web_real-008.yaml`
  - `tasks/config_web_real/config_web_real-009.yaml`
  - `tasks/config_web_real/config_web_real-011.yaml`
  - `tasks/config_web_real/config_web_real-012.yaml`
  - `tasks/config_web_real/config_web_real-013.yaml`
  - `tasks/config_web_real/config_web_real-014.yaml`
  - `tasks/config_web_real/config_web_real-015.yaml`
  - `tasks/config_web_real/config_web_real-016.yaml`
  - `tasks/config_web_real/config_web_real-017.yaml`
  - `tasks/config_web_real/config_web_real-018.yaml`
  - `tasks/config_web_real/config_web_real-019.yaml`
  - `tasks/config_web_real/config_web_real-020.yaml`
- `hf/Team-ACE__ToolACE`:
  - `data.json`
