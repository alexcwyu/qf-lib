# yfinance download-worker resource cleanup

Upstream: [yfinance](https://github.com/ranaroussi/yfinance). PyPI release: `1.7.0`. Local version: `1.7.0+ayu1`.

Original source archive: https://files.pythonhosted.org/packages/51/94/fefb0afc174ac1ce4f6b231c62ca30168ac29d8c937cab8d01a748d9cd0e/yfinance-1.7.0.tar.gz

Verified SHA256: `442f780d13d3e52fefa6c721c2c9bfee321078c1987d6585ec193b5c24382f8a`. Original license retained. No upstream tests are copied or changed.

Current upstream source was also verified at [`5cae563642b59f49adf6a04a5ad6744f8b0e084d`](https://raw.githubusercontent.com/ranaroussi/yfinance/5cae563642b59f49adf6a04a5ad6744f8b0e084d/yfinance/multi.py); SHA256 `61aa5ec181f26c134ed74661b9ed6644935a054d0543b7d1f5b67a1bc0e3dd83`. Its download worker still does not close thread-local cache databases.

The only behavior patch wraps `_download_one_threaded` in `try/finally` and closes each worker-owned timezone, cookie and ISIN cache connection through the existing database managers. Peewee reopens connections on later use. Download concurrency, requests, return values, error recording and progress behavior are preserved. Main-thread atexit cannot close another thread's SQLite connection; deterministic owner-thread cleanup fixes Python 3.13+ ResourceWarning failures without warning filters.

Use the repository uv workflow so `tool.uv.sources` selects this source. The sdist includes it; ordinary wheel installers do not interpret uv sources. Refresh by downloading the latest official source archive, verifying its published SHA256, retaining the license and reapplying only this cleanup. Retire the override once the upstream worker performs owner-thread cache cleanup and the existing complete QF-Lib suite passes.
