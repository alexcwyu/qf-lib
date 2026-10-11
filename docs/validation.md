# Validation evidence: qf-lib

Run date: 2026-10-12. Branch: `feature/ayu_develop`. Interpreter: `3.15.0 (main, Oct  9 2026, 15:11:47) [Clang 22.1.3 ]`.

| Check | Result |
|---|---|
| lock | passed |
| sync | passed |
| compile | passed |
| build | passed |
| tests | passed |

## Current result and compatibility decisions

- The complete supplied suite passes on managed Python 3.15.0: 876 passed, 109 preexisting skips (including one collection skip), exit0. Skips retain the upstream checks for unavailable Bloomberg/Quandl/Haver/other licensed services; none are introduced by maintenance.
- Managed Python 3.15.0 resolves and installs the complete extra/dev environment. Native cvxopt builds after installing SuiteSparse; WeasyPrint uses Pango/GLib.
- NumPy sign is imported from its public namespace; plotting uses public colormaps and loads the packaged qf style directly, preserving plotting behavior.
- Pandas copy-on-write updates write directly into owning frames, numeric portfolio/volume arrays retain mutable copies, factor intercept extraction uses iloc, and removed frequency aliases use their current equivalent values. Bloomberg missing numeric fields remain NaN.
- Internal return aggregation bypasses the deprecated public grouping entry point while that public API keeps its warning and behavior. The existing deprecated-API cases explicitly check the warning and retain their value assertions.
- The existing CSV fixture uses its supported dateformat=mixed option, and the existing crypto-client fixture mocks unused stock-client authentication. JWT fixtures retain expiration assertions with a valid-length test-only HS256 key. No cases are added or disabled.
- Verified latest yfinance1.7.0 source closes each worker-owned Peewee/SQLite cache connection in finally. Threaded requests, values, error recording and progress behavior are preserved. See vendor/yfinance/PROVENANCE.md and retained license. The existing Yahoo/related alpha subset passes all25 cases.
- The source archive includes vendor sources and uv.lock. Ordinary wheel installers do not interpret tool.uv.sources; use the documented uv checkout/sdist workflow to reproduce the dependency resource patch.
- Bloomberg blpapi3.26.9.1 is resolved from its official explicit index, including current ARM64 wheels. Normal uv compile-bytecode installation handles its existing docstring compile warnings; runtime pytest warning policy remains strict. The proprietary SDK license prohibits modification.
- WeasyPrint requires native Pango/GLib; brew install pango supplies these prerequisites and DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib exposes them to the managed macOS interpreter.
- Alpaca-py0.44.0 imports websockets.legacy, which deprecated since14. The optional Alpaca extra selects the latest compatible13.1 API family.
- The current Myst parser needs docutils<0.23; the docs extra retains that compatibility range. Existing Bloomberg BEAP APIs are preserved although upstream removed them.

Current unresolved checks:

All supplied checks recorded below passed.

## Latest full-suite output

```text
t using `QUANTFIN_SECRET` environment variable. Sample value of the env. variable:
{"quandl_key": "zW14dr45trz4up4d4juZ"}
To get the key, register an account at https://www.quandl.com
SKIPPED [1] src/qf_lib/tests/integration_tests/data_providers/quandl/test_quandl_table.py:74: `quandl_key` property was not found in the settings.
Set it using `QUANTFIN_SECRET` environment variable. Sample value of the env. variable:
{"quandl_key": "zW14dr45trz4up4d4juZ"}
To get the key, register an account at https://www.quandl.com
SKIPPED [1] src/qf_lib/tests/integration_tests/data_providers/quandl/test_quandl_table.py:64: `quandl_key` property was not found in the settings.
Set it using `QUANTFIN_SECRET` environment variable. Sample value of the env. variable:
{"quandl_key": "zW14dr45trz4up4d4juZ"}
To get the key, register an account at https://www.quandl.com
SKIPPED [1] src/qf_lib/tests/integration_tests/data_providers/quandl/test_quandl_table.py:115: `quandl_key` property was not found in the settings.
Set it using `QUANTFIN_SECRET` environment variable. Sample value of the env. variable:
{"quandl_key": "zW14dr45trz4up4d4juZ"}
To get the key, register an account at https://www.quandl.com
SKIPPED [1] src/qf_lib/tests/integration_tests/data_providers/quandl/test_quandl_table.py:105: `quandl_key` property was not found in the settings.
Set it using `QUANTFIN_SECRET` environment variable. Sample value of the env. variable:
{"quandl_key": "zW14dr45trz4up4d4juZ"}
To get the key, register an account at https://www.quandl.com
SKIPPED [1] src/qf_lib/tests/integration_tests/data_providers/quandl/test_quandl_table.py:86: `quandl_key` property was not found in the settings.
Set it using `QUANTFIN_SECRET` environment variable. Sample value of the env. variable:
{"quandl_key": "zW14dr45trz4up4d4juZ"}
To get the key, register an account at https://www.quandl.com
SKIPPED [1] src/qf_lib/tests/integration_tests/data_providers/quandl/test_quandl_table.py:96: `quandl_key` property was not found in the settings.
Set it using `QUANTFIN_SECRET` environment variable. Sample value of the env. variable:
{"quandl_key": "zW14dr45trz4up4d4juZ"}
To get the key, register an account at https://www.quandl.com
SKIPPED [1] src/qf_lib/tests/integration_tests/data_providers/quandl/test_quandl_timeseries.py:242: `quandl_key` property was not found in the settings.
Set it using `QUANTFIN_SECRET` environment variable. Sample value of the env. variable:
{"quandl_key": "zW14dr45trz4up4d4juZ"}
To get the key, register an account at https://www.quandl.com
SKIPPED [1] src/qf_lib/tests/integration_tests/data_providers/quandl/test_quandl_timeseries.py:225: `quandl_key` property was not found in the settings.
Set it using `QUANTFIN_SECRET` environment variable. Sample value of the env. variable:
{"quandl_key": "zW14dr45trz4up4d4juZ"}
To get the key, register an account at https://www.quandl.com
SKIPPED [1] src/qf_lib/tests/integration_tests/data_providers/quandl/test_quandl_timeseries.py:234: `quandl_key` property was not found in the settings.
Set it using `QUANTFIN_SECRET` environment variable. Sample value of the env. variable:
{"quandl_key": "zW14dr45trz4up4d4juZ"}
To get the key, register an account at https://www.quandl.com
SKIPPED [1] src/qf_lib/tests/integration_tests/data_providers/quandl/test_quandl_timeseries.py:86: `quandl_key` property was not found in the settings.
Set it using `QUANTFIN_SECRET` environment variable. Sample value of the env. variable:
{"quandl_key": "zW14dr45trz4up4d4juZ"}
To get the key, register an account at https://www.quandl.com
SKIPPED [1] src/qf_lib/tests/integration_tests/data_providers/quandl/test_quandl_timeseries.py:197: `quandl_key` property was not found in the settings.
Set it using `QUANTFIN_SECRET` environment variable. Sample value of the env. variable:
{"quandl_key": "zW14dr45trz4up4d4juZ"}
To get the key, register an account at https://www.quandl.com
SKIPPED [1] src/qf_lib/tests/integration_tests/data_providers/quandl/test_quandl_timeseries.py:214: `quandl_key` property was not found in the settings.
Set it using `QUANTFIN_SECRET` environment variable. Sample value of the env. variable:
{"quandl_key": "zW14dr45trz4up4d4juZ"}
To get the key, register an account at https://www.quandl.com
SKIPPED [1] src/qf_lib/tests/integration_tests/data_providers/quandl/test_quandl_timeseries.py:205: `quandl_key` property was not found in the settings.
Set it using `QUANTFIN_SECRET` environment variable. Sample value of the env. variable:
{"quandl_key": "zW14dr45trz4up4d4juZ"}
To get the key, register an account at https://www.quandl.com
SKIPPED [1] src/qf_lib/tests/integration_tests/data_providers/quandl/test_quandl_timeseries.py:179: `quandl_key` property was not found in the settings.
Set it using `QUANTFIN_SECRET` environment variable. Sample value of the env. variable:
{"quandl_key": "zW14dr45trz4up4d4juZ"}
To get the key, register an account at https://www.quandl.com
SKIPPED [1] src/qf_lib/tests/integration_tests/data_providers/quandl/test_quandl_timeseries.py:188: `quandl_key` property was not found in the settings.
Set it using `QUANTFIN_SECRET` environment variable. Sample value of the env. variable:
{"quandl_key": "zW14dr45trz4up4d4juZ"}
To get the key, register an account at https://www.quandl.com
SKIPPED [1] src/qf_lib/tests/integration_tests/data_providers/quandl/test_quandl_timeseries.py:112: `quandl_key` property was not found in the settings.
Set it using `QUANTFIN_SECRET` environment variable. Sample value of the env. variable:
{"quandl_key": "zW14dr45trz4up4d4juZ"}
To get the key, register an account at https://www.quandl.com
SKIPPED [1] src/qf_lib/tests/integration_tests/data_providers/quandl/test_quandl_timeseries.py:165: `quandl_key` property was not found in the settings.
Set it using `QUANTFIN_SECRET` environment variable. Sample value of the env. variable:
{"quandl_key": "zW14dr45trz4up4d4juZ"}
To get the key, register an account at https://www.quandl.com
SKIPPED [1] src/qf_lib/tests/integration_tests/data_providers/quandl/test_quandl_timeseries.py:153: `quandl_key` property was not found in the settings.
Set it using `QUANTFIN_SECRET` environment variable. Sample value of the env. variable:
{"quandl_key": "zW14dr45trz4up4d4juZ"}
To get the key, register an account at https://www.quandl.com
SKIPPED [1] src/qf_lib/tests/integration_tests/data_providers/quandl/test_quandl_timeseries.py:144: `quandl_key` property was not found in the settings.
Set it using `QUANTFIN_SECRET` environment variable. Sample value of the env. variable:
{"quandl_key": "zW14dr45trz4up4d4juZ"}
To get the key, register an account at https://www.quandl.com
SKIPPED [1] src/qf_lib/tests/integration_tests/data_providers/quandl/test_quandl_timeseries.py:104: `quandl_key` property was not found in the settings.
Set it using `QUANTFIN_SECRET` environment variable. Sample value of the env. variable:
{"quandl_key": "zW14dr45trz4up4d4juZ"}
To get the key, register an account at https://www.quandl.com
SKIPPED [1] src/qf_lib/tests/integration_tests/data_providers/quandl/test_quandl_timeseries.py:94: `quandl_key` property was not found in the settings.
Set it using `QUANTFIN_SECRET` environment variable. Sample value of the env. variable:
{"quandl_key": "zW14dr45trz4up4d4juZ"}
To get the key, register an account at https://www.quandl.com
SKIPPED [1] src/qf_lib/tests/integration_tests/data_providers/quandl/test_quandl_timeseries.py:76: `quandl_key` property was not found in the settings.
Set it using `QUANTFIN_SECRET` environment variable. Sample value of the env. variable:
{"quandl_key": "zW14dr45trz4up4d4juZ"}
To get the key, register an account at https://www.quandl.com
SKIPPED [1] src/qf_lib/tests/integration_tests/data_providers/quandl/test_quandl_timeseries.py:135: `quandl_key` property was not found in the settings.
Set it using `QUANTFIN_SECRET` environment variable. Sample value of the env. variable:
{"quandl_key": "zW14dr45trz4up4d4juZ"}
To get the key, register an account at https://www.quandl.com
SKIPPED [1] src/qf_lib/tests/integration_tests/data_providers/quandl/test_quandl_timeseries.py:126: `quandl_key` property was not found in the settings.
Set it using `QUANTFIN_SECRET` environment variable. Sample value of the env. variable:
{"quandl_key": "zW14dr45trz4up4d4juZ"}
To get the key, register an account at https://www.quandl.com
SKIPPED [1] src/qf_lib/tests/integration_tests/data_providers/test_haver.py:112: No Haver installed, skipping tests
SKIPPED [1] src/qf_lib/tests/integration_tests/data_providers/test_haver.py:126: No Haver installed, skipping tests
SKIPPED [1] src/qf_lib/tests/integration_tests/data_providers/test_haver.py:105: No Haver installed, skipping tests
SKIPPED [1] src/qf_lib/tests/integration_tests/data_providers/test_haver.py:133: No Haver installed, skipping tests
SKIPPED [1] src/qf_lib/tests/integration_tests/data_providers/test_haver.py:120: No Haver installed, skipping tests
SKIPPED [1] src/qf_lib/tests/integration_tests/data_providers/test_haver.py:144: No Haver installed, skipping tests
SKIPPED [1] src/qf_lib/tests/integration_tests/data_providers/test_haver.py:140: No Haver installed, skipping tests
SKIPPED [1] src/qf_lib/tests/integration_tests/data_providers/test_haver.py:74: No Haver installed, skipping tests
SKIPPED [1] src/qf_lib/tests/integration_tests/data_providers/test_haver.py:95: No Haver installed, skipping tests
SKIPPED [1] src/qf_lib/tests/integration_tests/data_providers/test_haver.py:56: No Haver installed, skipping tests
SKIPPED [1] src/qf_lib/tests/integration_tests/data_providers/test_haver.py:86: No Haver installed, skipping tests
SKIPPED [1] src/qf_lib/tests/manual_tests/test_strategies.py:33: No Bloomberg connection
SKIPPED [1] src/qf_lib/tests/manual_tests/test_strategies.py:41: No Bloomberg connection
SKIPPED [1] src/qf_lib/tests/manual_tests/test_strategies.py:49: No Bloomberg connection
================= 876 passed, 109 skipped in 622.82s (0:10:22) =================

```

## Exact commands and exit codes

Unsuccessful rows are retained as historical compatibility attempts; they are not claims that a current passing check remains blocked. Source-build probes use isolated temporary copies to preserve the selected repository environment.

| Command | Exit | Seconds | Evidence |
|---|---:|---:|---|
| `uv lock --upgrade --python 3.15` | 0 | 1.15 | [log](../../docs/maintenance-2026-10-12/qf-lib-lock-3.15.log) |
| `uv sync --all-extras --all-groups --python 3.15 --no-build --no-install-project` | 2 | 0.05 | [log](../../docs/maintenance-2026-10-12/qf-lib-wheel-probe-3.15.log) |
| `uv lock --upgrade --python 3.14` | 0 | 1.29 | [log](../../docs/maintenance-2026-10-12/qf-lib-lock-3.14.log) |
| `uv sync --all-extras --all-groups --python 3.14 --no-build --no-install-project` | 2 | 0.04 | [log](../../docs/maintenance-2026-10-12/qf-lib-wheel-probe-3.14.log) |
| `uv sync --all-extras --all-groups --python 3.14` | 0 | 3.49 | [log](../../docs/maintenance-2026-10-12/qf-lib-sync-3.14.log) |
| `uv build --python 3.14` | 0 | 7.27 | [log](../../docs/maintenance-2026-10-12/qf-lib-build.log) |
| `/Users/alex/.local/share/uv/python/cpython-3.14-macos-aarch64-none/bin/python3.14 -m compileall -q src` | 0 | 0.72 | [log](../../docs/maintenance-2026-10-12/qf-lib-compile.log) |
| `uv run --no-sync python -m pytest` | 2 | 12.72 | [log](../../docs/maintenance-2026-10-12/qf-lib-tests.log) |
| `uv run --no-sync python -m pytest` | 2 | 7.35 | [log](../../docs/maintenance-2026-10-12/qf-lib-tests-numpy-public-api.log) |
| `uv lock --upgrade --python 3.14` | 0 | 2.89 | [log](../../docs/maintenance-2026-10-12/qf-lib-lock-bloomberg-sdk.log) |
| `uv sync --all-extras --all-groups --python 3.14` | 0 | 1.46 | [log](../../docs/maintenance-2026-10-12/qf-lib-sync-bloomberg-sdk.log) |
| `uv run --no-sync python -m pytest` | 2 | 12.17 | [log](../../docs/maintenance-2026-10-12/qf-lib-tests-bloomberg-sdk.log) |
| `uv sync --all-extras --all-groups --python 3.14 --compile-bytecode` | 0 | 2.65 | [log](../../docs/maintenance-2026-10-12/qf-lib-sync-bloomberg-bytecode.log) |
| `uv run --no-sync python -m pytest` | 2 | 6.04 | [log](../../docs/maintenance-2026-10-12/qf-lib-tests-bloomberg-bytecode.log) |
| `brew install pango` | 0 | 9.05 | [log](../../docs/maintenance-2026-10-12/qf-lib-native-pango.log) |
| `uv lock --upgrade --python 3.14` | 0 | 1.09 | [log](../../docs/maintenance-2026-10-12/qf-lib-lock-alpaca-legacy-websockets.log) |
| `uv sync --all-extras --all-groups --python 3.14 --compile-bytecode` | 0 | 0.97 | [log](../../docs/maintenance-2026-10-12/qf-lib-sync-alpaca-legacy-websockets.log) |
| `env DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib uv run --no-sync python -m pytest` | 2 | 5.18 | [log](../../docs/maintenance-2026-10-12/qf-lib-tests-native-rendering-sdk.log) |
| `uv run --no-sync python -m compileall -q src` | 0 | 0.5 | [log](../../docs/maintenance-2026-10-12/qf-lib-compile-final.log) |
| `uv build --python 3.14` | 0 | 6.0 | [log](../../docs/maintenance-2026-10-12/qf-lib-build-final.log) |
| `uv run --no-sync python -c import sys,importlib.metadata,json; print(sys.version); print(json.dumps({d.metadata["Name"]: d.version for d in importlib.metadata.distributions()},indent=2,sort_keys=True))` | 0 | 0.18 | [log](../../docs/maintenance-2026-10-12/qf-lib-versions-final.log) |
| `env DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib uv run --no-sync python -m pytest` | 1 | 807.1 | [log](../../docs/maintenance-2026-10-12/qf-lib-tests-docstring-native-sdk.log) |
| `uv lock --upgrade --python 3.15` | 0 | 3.18 | [log](../../docs/maintenance-2026-10-12/qf-lib-lock-python315-source-supported.log) |
| `env CVXOPT_SUITESPARSE_INC_DIR=/opt/homebrew/include/suitesparse CVXOPT_SUITESPARSE_LIB_DIR=/opt/homebrew/lib uv sync --all-extras --all-groups --python 3.15 --compile-bytecode` | 0 | 8.15 | [log](../../docs/maintenance-2026-10-12/qf-lib-sync-python315-source-supported.log) |
| `env DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib uv run --no-sync python -m pytest src/qf_lib/tests/unit_tests` | 1 | 33.9 | [log](../../docs/maintenance-2026-10-12/qf-lib-tests-unit-current-scientific-apis.log) |
| `env DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib uv run --frozen --all-extras --all-groups python -m pytest src/qf_lib/tests/unit_tests -q` | 1 | 25.1 | [log](../../docs/maintenance-2026-10-12/qf-lib-tests-unit-pandas-api-fixes.log) |
| `env DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib uv run --frozen --all-extras --all-groups python -m pytest src/qf_lib/tests -v` | 1 | 601.91 | [log](../../docs/maintenance-2026-10-12/qf-lib-tests-python315-full-current-apis.log) |
| `uv lock --upgrade` | 0 | 3.26 | [log](../../docs/maintenance-2026-10-12/qf-lib-lock-yfinance-worker-cleanup.log) |
| `uv sync --frozen --all-extras --all-groups --compile-bytecode` | 0 | 0.98 | [log](../../docs/maintenance-2026-10-12/qf-lib-sync-yfinance-worker-cleanup.log) |
| `env DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib uv run --frozen --all-extras --all-groups python -m pytest src/qf_lib/tests/integration_tests/data_providers/yfinance_data_provider/test_yfinance_data_provider.py src/qf_lib/tests/unit_tests/backtesting/alpha_model/test_alpha_model.py -v` | 0 | 3.45 | [log](../../docs/maintenance-2026-10-12/qf-lib-tests-yfinance-owner-thread-cleanup.log) |
| `uv build` | 0 | 3.29 | [log](../../docs/maintenance-2026-10-12/qf-lib-build-python315-yfinance-final.log) |
| `uv run --frozen --all-extras --all-groups python -m compileall -q src vendor` | 0 | 0.73 | [log](../../docs/maintenance-2026-10-12/qf-lib-compile-python315-yfinance-final.log) |
| `uv run --frozen --all-extras --all-groups python -c import sys, importlib.metadata as m; print(sys.version); print('\n'.join(sorted(d.metadata['Name']+'=='+d.version for d in m.distributions())))` | 0 | 0.24 | [log](../../docs/maintenance-2026-10-12/qf-lib-versions-final.log) |
| `env DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib uv run --frozen --all-extras --all-groups python -m pytest src/qf_lib/tests -v` | 0 | 623.97 | [log](../../docs/maintenance-2026-10-12/qf-lib-tests-python315-full-final-cleanup.log) |
| `brew list --versions pango glib suite-sparse` | 0 | 0.93 | [log](../../docs/maintenance-2026-10-12/qf-lib-native-versions-final.log) |
| `uv run --frozen --all-extras --all-groups python /tmp/qf-artifact-verify.py` | 0 | 0.29 | [log](../../docs/maintenance-2026-10-12/qf-lib-artifact-content-final.log) |

The versions-final log records the exact interpreter patch release and every installed dependency version. The machine-readable [result](../../docs/maintenance-2026-10-12/qf-lib-result.json) includes branch/default ancestry, status, artifacts and unresolved checks.

## Dependency floor refresh

| Before | After |
|---|---|

The table records the initial metadata refresh. Later compatibility constraints and vendor sources are explained above and the final authoritative requirements are in [pyproject.toml](../pyproject.toml) and [uv.lock](../uv.lock). No test cases were added, removed or disabled. Existing deprecated-API cases retain their assertions while explicitly checking the documented warning.
