define e = Character("Eileen")

label start:
    scene bg room
    show eileen happy

    e "クリッククラッカーへようこそ！"
    e "ここでは、ハッキングバトルを楽しむことができます。"

    menu:
        "ゲームを始める":
            jump game_start

        "終了する":
            jump end

label game_start:
    e "さあ、ハッキングバトルを始めましょう！"
    return
