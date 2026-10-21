# opd-lab-assets

Unmodified copies of small, openly licensed datasets used by the OPD lab's tool-call experiments
([opd-blackwell-runbook](https://github.com/yang3121099/opd-blackwell-runbook)), kept here so that a training node that
can reach GitHub but not the Hugging Face hub can `git clone` them. Each dataset stays under its own license; nothing
was added to or changed in the data. Files whose fixtures hold strings shaped like live API keys or tokens
(refused by GitHub's push protection) are left out and listed in each folder's `LEFT_OUT.txt`.

| folder | source | revision | license | files | size |
|---|---|---|---|---:|---:|
| `hf/AIcell__Auto-ClawEval-mini` | [AIcell/Auto-ClawEval-mini](https://huggingface.co/datasets/AIcell/Auto-ClawEval-mini) | `472e6a0824c6` | MIT | 130 | 2.6 MB |
| `hf/AIcell__Auto-ClawEval` | [AIcell/Auto-ClawEval](https://huggingface.co/datasets/AIcell/Auto-ClawEval) | `a1b2e95ab740` | MIT | 1264 | 11.8 MB |
| `hf/gorilla-llm__Berkeley-Function-Calling-Leaderboard` | [gorilla-llm/Berkeley-Function-Calling-Leaderboard](https://huggingface.co/datasets/gorilla-llm/Berkeley-Function-Calling-Leaderboard) | `61fc0608cfd8` | Apache-2.0 | 51 | 11.7 MB |

Layout: `hf/<owner>__<name>/` holds the files of that dataset revision, its dataset card (`README.md`) and `SOURCE.md`
(source, revision, license). The license texts are in `LICENSES/` (MIT, Apache-2.0); the MIT notice names the original
authors through each folder's `SOURCE.md`. `MANIFEST.sha256` lists every file with its SHA-256.

Use: `git clone --depth 1 https://github.com/yang3121099/opd-lab-assets` (about 26 MB).

If you are an author of one of these datasets and want it removed or attributed differently, please open an issue.
