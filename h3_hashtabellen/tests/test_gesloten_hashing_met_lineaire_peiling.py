import pytest

from h3_hashtabellen.gesloten_hashing_met_lineaire_peiling import HashSet


@pytest.mark.timeout(2)
def test_index_of_geeft_min_een_terug_voor_leeg():
    h = HashSet(max_size=10)
    # leeg
    assert h.index_of(123) == -1

@pytest.mark.timeout(2)
def test_add_zonder_botsingen_elementen_op_juiste_index():
    h = HashSet(max_size=10)

    # toevoegen en terugvinden
    i10 = h.add(10)
    i15 = h.add(15)
    i29 = h.add(29)

    assert 0 <= i10 < 10
    assert 0 <= i15 < 10
    assert 0 <= i29 < 10

    assert h.index_of(10) == i10
    assert h.index_of(15) == i15
    assert h.index_of(29) == i29


@pytest.mark.timeout(2)
def test_add_gaat_correct_om_met_botsingen():
    # Met integers is hash(x) == x, dus modulo is voorspelbaar
    h = HashSet(max_size=7)
    # 0, 7, 14 botsen allemaal op index 0
    i0 = h.add(0)    # -> index 0
    i7 = h.add(7)    # -> index 1
    i14 = h.add(14)  # -> index 2

    assert (i0, i7, i14) == (0, 1, 2)
    assert h.index_of(0) == 0
    assert h.index_of(7) == 1
    assert h.index_of(14) == 2


@pytest.mark.timeout(2)
def test_add_met_wraparound_en_hergebruik_van_geleegde_ppsitie():
    # wraparound = je komt aan het einde van de tabel en moet verder
    # vanaf het begin van de tabel
    h = HashSet(max_size=5)

    # Vul aaneengesloten indices op 0..3
    # 0%5=0, 5%5=0 -> 1, 10%5=0 -> 2, 15%5=0 -> 3
    a = h.add(0)    # 0
    b = h.add(5)    # 1
    c = h.add(10)   # 2
    d = h.add(15)   # 3
    assert (a, b, c, d) == (0, 1, 2, 3)

    # delete element op index 1 (waarde 5) -> flag
    assert h.delete(5) is True
    assert h.index_of(5) == -1

    # bestaande elementen blijven vindbaar, dankzij correct gebruik flag
    assert h.index_of(0) == 0
    assert h.index_of(10) == 2
    assert h.index_of(15) == 3

    # wrap-around check: toevoegen van 20 (hash 0) loopt tegen 0, gaat naar 1 (flag reused)
    e = h.add(20)
    assert e == 1
    assert h.index_of(20) == 1


@pytest.mark.timeout(2)
def test_delete_verwijdert_en_index_of_gebruikt_flag_correct():
    h = HashSet(max_size=5)
    # 0, 5, 10 -> indices 0,1,2
    h.add(0)
    h.add(5)
    h.add(10)
    # verwijder 5 (index 1), maar 10 moet nog vindbaar zijn (door deleted heen)
    assert h.delete(5) is True
    assert h.index_of(10) == 2
    # 5 is niet meer aanwezig
    assert h.index_of(5) == -1


@pytest.mark.timeout(2)
def test_tabel_vol_raises_valueerror():
    h = HashSet(max_size=3)
    h.add(1)
    h.add(2)
    h.add(3)
    with pytest.raises(ValueError):
        h.add(4)  # set is vol


@pytest.mark.timeout(2)
def test_delete_geeft_false_voor_niet_bestaand_element():
    h = HashSet(max_size=4)
    h.add(1)
    assert h.delete(999) is False
    # bestaand element blijft vindbaar
    assert h.index_of(1) != -1
