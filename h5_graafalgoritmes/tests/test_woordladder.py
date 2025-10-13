import pytest
from pathlib import Path

from h5_graafalgoritmes.woordladder import (
    precies_een_verschillend,
    maak_graaf,
    kortste_pad,
    geef_pad,
)

@pytest.mark.timeout(1)
def test_precies_een_verschillend():
    assert precies_een_verschillend("span", "spat") is True
    assert precies_een_verschillend("test", "tast") is True
    assert precies_een_verschillend("test", "test") is False
    assert precies_een_verschillend("test", "testje") is False
    assert precies_een_verschillend("testje", "test") is False
    assert precies_een_verschillend("TEST", "test") is False


@pytest.mark.timeout(1)
def test_maak_graaf_2letters():
    words = ["aa", "ab", "ac", "ad",
             "ba", "bb", "bc", "bd",
             "ca", "cb", "cc", "cd",
             "da", "db", "dc", "dd"]
    g = maak_graaf(words)
    expected = {
        'aa': {'ac', 'ca', 'ab', 'ba', 'da', 'ad'},
        'ab': {'aa', 'ac', 'cb', 'db', 'bb', 'ad'},
        'ac': {'aa', 'dc', 'ab', 'bc', 'cc', 'ad'},
        'ad': {'ac', 'ab', 'dd', 'cd', 'bd', 'aa'},
        'ba': {'ca', 'bc', 'bd', 'da', 'bb', 'aa'},
        'bb': {'ab', 'bc', 'ba', 'bd', 'cb', 'db'},
        'bc': {'ac', 'dc', 'ba', 'bd', 'bb', 'cc'},
        'bd': {'dd', 'bc', 'cd', 'ba', 'bb', 'ad'},
        'ca': {'cd', 'ba', 'da', 'cb', 'cc', 'aa'},
        'cb': {'ca', 'ab', 'cd', 'db', 'bb', 'cc'},
        'cc': {'ac', 'ca', 'dc', 'bc', 'cd', 'cb'},
        'cd': {'ca', 'dd', 'bd', 'cb', 'cc', 'ad'},
        'da': {'ca', 'dc', 'dd', 'ba', 'db', 'aa'},
        'db': {'dc', 'ab', 'cb', 'dd', 'da', 'bb'},
        'dc': {'ac', 'dd', 'bc', 'da', 'db', 'cc'},
        'dd': {'dc', 'cd', 'bd', 'da', 'db', 'ad'},
    }
    assert g == expected


@pytest.mark.timeout(1)
def test_kortste_pad_voorbeeld_uit_opgave():
    words = ["aa", "ab", "ac", "ad",
             "ba", "bb", "bc", "bd",
             "ca", "cb", "cc", "cd",
             "da", "db", "dc", "dd"]
    graaf = maak_graaf(words)
    pred = kortste_pad(graaf, "aa")
    expected_pred = {
        'aa': 'aa', 'ab': 'aa', 'ac': 'aa', 'ad': 'aa',
        'ba': 'aa', 'bb': 'ab', 'bc': 'ac', 'bd': 'ad',
        'ca': 'aa', 'cb': 'ab', 'cc': 'ac', 'cd': 'ad',
        'da': 'aa', 'db': 'ab', 'dc': 'ac', 'dd': 'ad'
    }
    assert pred == expected_pred


@pytest.mark.timeout(1)
def test_geef_pad_2letters():
    words = ["aa", "ab", "ac", "ad",
             "ba", "bb", "bc", "bd",
             "ca", "cb", "cc", "cd",
             "da", "db", "dc", "dd"]
    g = maak_graaf(words)
    pred = kortste_pad(g, "aa")
    assert geef_pad(pred, "dd") == ['aa', 'ad', 'dd']
    assert geef_pad(pred, "aa") == ['aa']
    assert geef_pad(pred, "ba") == ['aa', 'ba']



@pytest.mark.timeout(50)  # maak_graaf is O(n^2) op 5757 woorden: geef wat tijd
def test_scenario_met_uitgebreid_woordenboek():
   
   # 1) woordenlijst laden
    current_folder = Path(__file__).parent
    words_path = current_folder / "sgb-words.txt"
    words = [w.strip() for w in words_path.read_text(encoding="utf-8").splitlines()]
    assert len(words) == 5757  # controle: alle woorden correct ingeladen?

    # 2) graaf bouwen
    graaf = maak_graaf(words)

    # 3) tests uitvoeren

    # test enkele buur-sets
    assert graaf['which'] == {'whish'}
    assert graaf['whish'] == {'whisk', 'shish', 'which', 'whist'}
    assert graaf['shish'] == {'whish', 'shush', 'swish'}
    assert graaf['shush'] == {'shish', 'slush'}
    assert graaf['slush'] == {'shush', 'plush', 'slash', 'slosh', 'flush', 'blush'}
    assert graaf['blush'] == {'brush', 'plush', 'slush', 'flush', 'blash'}

    # test kortste paden vanaf 'which'
    pred = kortste_pad(graaf, 'which')
    assert pred['blush'] == 'slush'
    assert pred['slush'] == 'shush'

    # test pad van 'which' naar 'blush'
    assert geef_pad(pred, 'blush') == ['which', 'whish', 'shish', 'shush', 'slush', 'blush']

    # aantal woorden bereikbaar uit 'which'
    connected_count = sum(1 for w in words if pred[w] is not None)
    assert connected_count == 4493

    # alfabetisch kleinste en grootste woord NIET bereikbaar uit 'which'
    not_connected_sorted = sorted([w for w in words if pred[w] is None])
    assert not_connected_sorted[0] == 'aargh'
    assert not_connected_sorted[-1] == 'zowie'

    # buurinfo voor 'aargh' en 'zowie'
    assert graaf['aargh'] == set()
    assert graaf['zowie'] == {'bowie'}

    # woorden met pad naar 'zowie'
    pred2 = kortste_pad(graaf, 'zowie')
    reachable_zowie = sorted([w for w in words if pred2[w] is not None])
    assert reachable_zowie == ['bogie', 'bowie', 'dogie', 'doxie', 'movie', 'moxie', 'zowie']
