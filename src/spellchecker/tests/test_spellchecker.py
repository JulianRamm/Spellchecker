from app.spellchecker import SpellChecker


def test_spell_check_sentence_without_accents():
    instance = SpellChecker()
    sentence = 'hopinion'
    assert 'opinión' == instance.spell_check_sentence(sentence)

    sentence = 'fabor guardar cilencio para no molestar'
    assert 'favor guardar silencio para no molestar' == instance.spell_check_sentence(sentence)

    sentence = 'un lgar para la hopinion'
    assert 'un lugar para la opinión' == instance.spell_check_sentence(sentence)

    sentence = 'el Arebol del día'
    assert 'el arrebol del día' == instance.spell_check_sentence(sentence)

    sentence = 'Rezpeto por la educasión'
    assert 'Respeto por la educación' == instance.spell_check_sentence(sentence)

    sentence = 'RTe encanta conduzir'
    assert 'Te encanta conducir' == instance.spell_check_sentence(sentence)

    sentence = 'HOy ay karne azada frezca siga pa dentro'
    assert 'Hoy ay carne azada fresca siga la dentro' == instance.spell_check_sentence(sentence)

    sentence = 'En mi ezcuela no enseñan a escrivir ni a ler'
    assert 'En mi escuela no enseñan a escribir ni a le' == instance.spell_check_sentence(sentence)

    sentence = 'él no era una persona de fiar pues era un mentirozo'
    assert 'él no era una persona de fiar pues era un mentiroso' == instance.spell_check_sentence(sentence)


def test_spell_check_sentence_with_accents():
    instance = SpellChecker()
    sentence = 'Él, no era una persona de fiar. Pues era un mentirozo.'
    assert 'Él, no era una persona de fiar. Pues era un mentiroso.' == instance.spell_check_sentence(sentence)

    sentence = 'él, no era una persona de fiar pues era un mentirozo'
    assert 'él, no era una persona de fiar pues era un mentiroso' == instance.spell_check_sentence(sentence)

    sentence = 'No era una persona de fiar pues era un mentirozo'
    assert 'No era una persona de fiar pues era un mentiroso' == instance.spell_check_sentence(sentence)

    sentence = 'trabaja de dia'
    assert 'trabaja de día' == instance.spell_check_sentence(sentence)