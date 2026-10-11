# qf-lib: portable verification records

Full raw logs are retained in the workspace maintenance evidence, not distributed here. Hashes identify those original logs. A successful build or selected test subset does not imply a full test-suite pass. Commands containing <workspace> describe the original execution environment.

[Machine-readable records](verification.json) · [Repository validation summary](../validation.md)

## Executed commands

| Check | Exit | Duration | Command | Outcomes |
| --- | ---: | ---: | --- | --- |
| artifact-content-final | 0 | 0.29s | `uv run --frozen --all-extras --all-groups python /tmp/qf-artifact-verify.py` | See exit status; no test-count assertion. |
| build | 0 | 7.27s | `uv build --python 3.14` | Successfully built dist/qf_lib-4.0.5.dev4+g6807f62f9.d20251115.tar.gz<br>Successfully built dist/qf_lib-4.0.5.dev4+g6807f62f9.d20251115-py3-none-any.whl |
| build-final | 0 | 6.0s | `uv build --python 3.14` | Successfully built dist/qf_lib-4.0.5.dev4+g6807f62f9.d20251115.tar.gz<br>Successfully built dist/qf_lib-4.0.5.dev4+g6807f62f9.d20251115-py3-none-any.whl |
| build-python315-yfinance-final | 0 | 3.29s | `uv build` | Successfully built dist/qf_lib-4.0.5.dev4+g6807f62f9.d20251115.tar.gz<br>Successfully built dist/qf_lib-4.0.5.dev4+g6807f62f9.d20251115-py3-none-any.whl |
| compile | 0 | 0.72s | `/Users/alex/.local/share/uv/python/cpython-3.14-macos-aarch64-none/bin/python3.14 -m compileall -q src` | See exit status; no test-count assertion. |
| compile-final | 0 | 0.5s | `uv run --no-sync python -m compileall -q src` | See exit status; no test-count assertion. |
| compile-python315-yfinance-final | 0 | 0.73s | `uv run --frozen --all-extras --all-groups python -m compileall -q src vendor` | See exit status; no test-count assertion. |
| lock-3.14 | 0 | 1.29s | `uv lock --upgrade --python 3.14` | See exit status; no test-count assertion. |
| lock-3.15 | 0 | 1.15s | `uv lock --upgrade --python 3.15` | See exit status; no test-count assertion. |
| lock-alpaca-legacy-websockets | 0 | 1.09s | `uv lock --upgrade --python 3.14` | See exit status; no test-count assertion. |
| lock-bloomberg-sdk | 0 | 2.89s | `uv lock --upgrade --python 3.14` | See exit status; no test-count assertion. |
| lock-python315-source-supported | 0 | 3.18s | `uv lock --upgrade --python 3.15` | See exit status; no test-count assertion. |
| lock-yfinance-worker-cleanup | 0 | 3.26s | `uv lock --upgrade` | See exit status; no test-count assertion. |
| native-pango | 0 | 9.05s | `brew install pango` | See exit status; no test-count assertion. |
| native-versions-final | 0 | 0.93s | `brew list --versions pango glib suite-sparse` | See exit status; no test-count assertion. |
| sync-3.14 | 0 | 3.49s | `uv sync --all-extras --all-groups --python 3.14` | See exit status; no test-count assertion. |
| sync-alpaca-legacy-websockets | 0 | 0.97s | `uv sync --all-extras --all-groups --python 3.14 --compile-bytecode` | See exit status; no test-count assertion. |
| sync-bloomberg-bytecode | 0 | 2.65s | `uv sync --all-extras --all-groups --python 3.14 --compile-bytecode` | See exit status; no test-count assertion. |
| sync-bloomberg-sdk | 0 | 1.46s | `uv sync --all-extras --all-groups --python 3.14` | See exit status; no test-count assertion. |
| sync-python315-source-supported | 0 | 8.15s | `env CVXOPT_SUITESPARSE_INC_DIR=/opt/homebrew/include/suitesparse CVXOPT_SUITESPARSE_LIB_DIR=/opt/homebrew/lib uv sync --all-extras --all-groups --python 3.15 --compile-bytecode` | See exit status; no test-count assertion. |
| sync-yfinance-worker-cleanup | 0 | 0.98s | `uv sync --frozen --all-extras --all-groups --compile-bytecode` | See exit status; no test-count assertion. |
| tests | 2 | 12.72s | `uv run --no-sync python -m pytest` | See exit status; no test-count assertion. |
| tests-bloomberg-bytecode | 2 | 6.04s | `uv run --no-sync python -m pytest` | See exit status; no test-count assertion. |
| tests-bloomberg-sdk | 2 | 12.17s | `uv run --no-sync python -m pytest` | See exit status; no test-count assertion. |
| tests-docstring-native-sdk | 1 | 807.1s | `env DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib uv run --no-sync python -m pytest` | 73 failed, 780 passed, 109 skipped, 23 errors, 29 subtests passed in 804.28s (0:13:24) |
| tests-native-rendering-sdk | 2 | 5.18s | `env DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib uv run --no-sync python -m pytest` | See exit status; no test-count assertion. |
| tests-numpy-public-api | 2 | 7.35s | `uv run --no-sync python -m pytest` | See exit status; no test-count assertion. |
| tests-python315-full-current-apis | 1 | 601.91s | `env DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib uv run --frozen --all-extras --all-groups python -m pytest src/qf_lib/tests -v` | ============ 2 failed, 874 passed, 109 skipped in 600.65s (0:10:00) ============ |
| tests-python315-full-final-cleanup | 0 | 623.97s | `env DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib uv run --frozen --all-extras --all-groups python -m pytest src/qf_lib/tests -v` | ================= 876 passed, 109 skipped in 622.82s (0:10:22) ================= |
| tests-unit-current-scientific-apis | 1 | 33.9s | `env DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib uv run --no-sync python -m pytest src/qf_lib/tests/unit_tests` | 21 failed, 788 passed, 23 errors, 14 subtests passed in 32.69s |
| tests-unit-pandas-api-fixes | 1 | 25.1s | `env DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib uv run --frozen --all-extras --all-groups python -m pytest src/qf_lib/tests/unit_tests -q` | See exit status; no test-count assertion. |
| tests-yfinance-owner-thread-cleanup | 0 | 3.45s | `env DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib uv run --frozen --all-extras --all-groups python -m pytest src/qf_lib/tests/integration_tests/data_providers/yfinance_data_provider/test_yfinance_data_provider.py src/qf_lib/tests/unit_tests/backtesting/alpha_model/test_alpha_model.py -v` | ============================== 25 passed in 2.78s ============================== |
| versions-final | 0 | 0.24s | `uv run --frozen --all-extras --all-groups python -c import sys, importlib.metadata as m; print(sys.version); print('\n'.join(sorted(d.metadata['Name']+'=='+d.version for d in m.distributions())))` | See exit status; no test-count assertion. |
| wheel-probe-3.14 | 2 | 0.04s | `uv sync --all-extras --all-groups --python 3.14 --no-build --no-install-project` | See exit status; no test-count assertion. |
| wheel-probe-3.15 | 2 | 0.05s | `uv sync --all-extras --all-groups --python 3.15 --no-build --no-install-project` | See exit status; no test-count assertion. |
