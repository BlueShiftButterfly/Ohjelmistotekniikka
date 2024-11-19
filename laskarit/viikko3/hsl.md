## HSL, sekvenssidiagrammi

```mermaid
sequenceDiagram
    participant main
    create participant laitehallinto
    create participant rautatietori
    create participant ratikka6
    create participant bussi244

    main->>laitehallinto: HKLLaitehallinto()
    main->>rautatietori: Lataajalaite()
    main->>ratikka6: Lukijalaite()
    main->>bussi244: Lukijalaite()

    main->>laitehallinto: lisaa_lataaja(rautatietori)
    main->>laitehallinto: lisaa_lukija_(ratikka6)
    main->>laitehallinto: lisaa_lukija(bussi244)

    create participant lippu_luukku

    main->>lippu_luukku: Kioski()

    create participant kallen_kortti

    lippu_luukku->>kallen_kortti: osta_matkakortti("Kalle)

    main->>rautatietori: lataa_arvoa(kallen_kortti)
    main->>ratikka6: osta_lippu(kallen_kortti, 0)
    main->>bussi244: osta_lippu(kallen_kortti, 2)
```