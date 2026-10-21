# opd-lab-assets

Copies of small, openly licensed datasets used by the OPD lab's tool-call experiments
([opd-blackwell-runbook](https://github.com/yang3121099/opd-blackwell-runbook)), kept here so that a training node that
can reach GitHub but not the Hugging Face hub can `git clone` them. Each dataset stays under its own license. The data is
unmodified except for one documented change: strings shaped like live API keys or tokens (fixtures of Auto-ClawEval's
safety tasks, two default values in ToolACE's tool schemas) are replaced by placeholders of the same length and provider
prefix that contain FAKE, consistently in every file, so the tasks keep working; see `REPLACED.md`.

| folder | source | revision | license | files | size | modified |
|---|---|---|---|---:|---:|---|
| `hf/AIcell__Auto-ClawEval-mini` | [AIcell/Auto-ClawEval-mini](https://huggingface.co/datasets/AIcell/Auto-ClawEval-mini) | `472e6a0824c6` | MIT | 136 | 2.7 MB | yes, see REPLACED.md |
| `hf/AIcell__Auto-ClawEval` | [AIcell/Auto-ClawEval](https://huggingface.co/datasets/AIcell/Auto-ClawEval) | `a1b2e95ab740` | MIT | 1338 | 12.4 MB | yes, see REPLACED.md |
| `hf/gorilla-llm__Berkeley-Function-Calling-Leaderboard` | [gorilla-llm/Berkeley-Function-Calling-Leaderboard](https://huggingface.co/datasets/gorilla-llm/Berkeley-Function-Calling-Leaderboard) | `61fc0608cfd8` | Apache-2.0 | 51 | 11.7 MB | no |
| `hf/Team-ACE__ToolACE` | [Team-ACE/ToolACE](https://huggingface.co/datasets/Team-ACE/ToolACE) | `6bda777c88d2` | Apache-2.0 | 2 | 37.2 MB | yes, see REPLACED.md |

Layout: `hf/<owner>__<name>/` holds the files of that dataset revision, its dataset card (`README.md`) and `SOURCE.md`
(source, revision, license, changes). The license texts are in `LICENSES/` (MIT, Apache-2.0); the MIT notice names the
original authors through each folder's `SOURCE.md`. `MANIFEST.sha256` lists every file with its SHA-256.

Use: `git clone --depth 1 https://github.com/yang3121099/opd-lab-assets` (about 64 MB).

If you are an author of one of these datasets and want it removed or attributed differently, please open an issue.
