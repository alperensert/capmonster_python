# Changelog

## [5.0.0](https://github.com/alperensert/capmonster_python/compare/v4.0.0...v5.0.0) (2026-03-15)


### ⚠ BREAKING CHANGES

* default retry_delay changed from 1.0 to 2.0 seconds.

### Features

* add context manager, solve() convenience, configurable polling, multi-Python CI ([5399fbb](https://github.com/alperensert/capmonster_python/commit/5399fbb5fcd34489d00b441555426825a0a95ce2))
* add FunCaptcha, Amazon WAF, reCAPTCHA v3 Enterprise, and Cloudflare Waiting Room ([b939c7b](https://github.com/alperensert/capmonster_python/commit/b939c7bfa0b8e32a7f71ae89ad53f2fae257773f))
* add MTCaptcha, Yidun, Altcha, Castle, and TSPD task types ([221aa0e](https://github.com/alperensert/capmonster_python/commit/221aa0e9912b943b8daa99774259be4458eefd03))
* add RecaptchaClickTask, HuntTask, and missing API fields ([eb38897](https://github.com/alperensert/capmonster_python/commit/eb38897fac930f89c79bd322ce9320687f424e1c))
* add reportIncorrect and getUserAgent client methods ([152dc97](https://github.com/alperensert/capmonster_python/commit/152dc978537bc774be99d0bfc4f75262d8a27202))


### Bug Fixes

* **ci:** add respx to test dependencies ([1976b6f](https://github.com/alperensert/capmonster_python/commit/1976b6fc2da0c98e6fdfbd78cf500e37095fa191))
* **ci:** specify release-please config and manifest paths ([5fb508a](https://github.com/alperensert/capmonster_python/commit/5fb508af7a2cfa938dcc819a357a40a22e9fe3b0))
* resolve test function shadowing, remove dead code, and cleanup ([4fcf311](https://github.com/alperensert/capmonster_python/commit/4fcf3119eb9b3deb85b852d8ac8fc589e9574fa2))


### Documentation

* update README and API reference for new features ([c8793f6](https://github.com/alperensert/capmonster_python/commit/c8793f66e3a844aca78b6f113e4ed99b72004a67))

## [4.0.0](https://github.com/alperensert/capmonster_python/compare/v3.2.0...v4.0.0) (2025-04-30)


### ⚠ BREAKING CHANGES

* API usage has completely changed from v3.2 to v4.0. All task creation methods now rely on structured payloads and typed clients.

### Features

* full rewrite with async support, pydantic v2 and modern architecture ([#72](https://github.com/alperensert/capmonster_python/issues/72)) ([bd9e40d](https://github.com/alperensert/capmonster_python/commit/bd9e40dd4ca22d757ed248d2f6903d5b38e0c960))


### Documentation

* add features section to documentation index ([17efb36](https://github.com/alperensert/capmonster_python/commit/17efb361da78aebd1e2395fb2d09aeea4fc36242))

## [3.2.0](https://github.com/alperensert/capmonster_python/compare/v3.1.0...v3.2.0) (2024-04-27)


### Features

* add amazon waf task support ([c78ff56](https://github.com/alperensert/capmonster_python/commit/c78ff5654b7ded310e5e647e7052712d7870e5f7))

## [3.1.0](https://github.com/alperensert/capmonster_python/compare/v3.0.0...v3.1.0) (2024-04-17)


### Features

* TenDI task ([#66](https://github.com/alperensert/capmonster_python/issues/66)) ([261638d](https://github.com/alperensert/capmonster_python/commit/261638d2f73c4a95840f1febc697e7162906a109))

## [3.0.0](https://github.com/alperensert/capmonster_python/compare/v2.6.2...v3.0.0) (2024-04-17)


### ⚠ BREAKING CHANGES

* fixing the TurnstileTask class call and adding usage examples ([#64](https://github.com/alperensert/capmonster_python/issues/64))

### Bug Fixes

* fixing the TurnstileTask class call and adding usage examples ([#64](https://github.com/alperensert/capmonster_python/issues/64)) ([a159818](https://github.com/alperensert/capmonster_python/commit/a15981829e0175978678f0d0995cbba001dc582d))
