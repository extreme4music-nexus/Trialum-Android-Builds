# Trialum — Android Build Center

**Public Android CI infrastructure · unsigned APKs · local-only signing**

Ова репозиториум е јавен **Android build-центар** за Trialum. Тој е
одделен од приватниот развоен репозиториум и од
[јавниот бета-канал](https://github.com/extreme4music-nexus/trialum-beta).

## Што прави

- Со GitHub Actions рачно компајлира **три непотпишани** Android варијанти:
  `release`, `signqa`, `signdebug`.
- Изворот мора да биде **веќе јавен commit во овој репозиториум**,
  избран од сопственикот со целосен SHA, не автоматски преземен од приватниот проект.
- Ги тестира проверките за играта и Android build-от, ги проверува package IDs,
  и создава SHA-256 листа и build provenance.
- Ги објавува само **unsigned build candidates** како GitHub Actions артефакти
  за преземање и **локално потпишување од сопственикот**.

**Ова репо не потпишува APK, не содржи keystore или Play Store credentials,
не објавува во Play Store и не прави автоматско огледало од приватниот Trialum.**

## Manual Android build

1. Отвори [Actions](https://github.com/extreme4music-nexus/Trialum-Android-Builds/actions)
   и избери **Trialum Android - unsigned builds**.
2. Кликни **Run workflow** на `main`.
3. Внеси целосен, веќе јавен, одобрен **40-карактерен source commit SHA**
   што содржи `snapshot/android-template` и `snapshot/tests`.
4. Потврди дека дозволуваш изворната снимка да остане јавна.
5. По успешен build преземи го `Trialum-unsigned-Android-...` артефактот.
   APK се **UNSIGNED — НЕ СЕ ПОТПИШАНИ**.
6. Потпиши на сопствениот компјутер според
   [docs/LOCAL_SIGNING.md](docs/LOCAL_SIGNING.md). Приватниот клуч никогаш
   не го поставувај на GitHub.

Еден постар LW-C CI snapshot веќе постои на гранката
`ci/lw-c-android-unsigned-20261113`. **Таа гранка е јавна**, а претходниот
workflow има успешно компајлирано три непотпишани Android кандидати.
Ова не е одобрение за Play Store или јавна бета. Не се додаваат нови
development снимки без изречна одлука на сопственикот.

## Project rules

- [BUILD_POLICY.md](BUILD_POLICY.md) — source, automation and signing boundaries
- [docs/LOCAL_SIGNING.md](docs/LOCAL_SIGNING.md) — secure local signing
- [SECURITY.md](SECURITY.md) — security contact and prohibitions
- [docs/PRIOR_LICENSES.md](docs/PRIOR_LICENSES.md) — earlier GPL/MIT releases and rights
- [LICENSE](LICENSE) — new owner-controlled build infrastructure only

**The GitHub-hosted build is not a Google Play release or signing service.**
The owner retains final approval over all official release decisions.

Copyright © 2026 Toni Cvetkovski, for original Trialum material owned by him.
All previous third-party and existing license grants remain in effect.
