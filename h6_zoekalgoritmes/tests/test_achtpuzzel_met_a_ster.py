import pytest

from h6_zoekalgoritmes.achtpuzzel_met_a_ster import (
    AchtPuzzel,
    Plan,
    a_ster_zoeken
)

@pytest.mark.timeout(2)
def test_achtpuzzel():
    puzzel = AchtPuzzel()
    assert puzzel.bord == '123456780'
    
    puzzel = AchtPuzzel('678405123')
    assert puzzel.bord == '678405123'

@pytest.mark.timeout(2)
def test_opvolgers():
    puzzel = AchtPuzzel()
    assert sorted(puzzel.opvolgers()) == [('B', AchtPuzzel(bord='123450786')), ('L', AchtPuzzel(bord='123456708'))]

    puzzel = AchtPuzzel("123450786")
    assert sorted(puzzel.opvolgers()) == [('B', AchtPuzzel(bord='120453786')), ('L', AchtPuzzel(bord='123405786')), ('O', AchtPuzzel(bord='123456780'))]

    puzzel = AchtPuzzel("678405123")
    assert sorted(puzzel.opvolgers()) == [('B', AchtPuzzel(bord='608475123')), ('L', AchtPuzzel(bord='678045123')), ('O', AchtPuzzel(bord='678425103')), ('R', AchtPuzzel(bord='678450123'))]

@pytest.mark.timeout(2)
def test_aantal_verkeerd():
    s1 = AchtPuzzel("724506831")
    s2 = AchtPuzzel("012345678")
    s3 = AchtPuzzel("724560831")
    assert s1.aantal_verkeerd(s2) == 8
    assert s2.aantal_verkeerd(s1) == 8
    assert s1.aantal_verkeerd(s1) == 0
    assert s1.aantal_verkeerd(s3) == 1
    assert s3.aantal_verkeerd(s1) == 1

@pytest.mark.timeout(2)
def test_manhattan():
    s1 = AchtPuzzel("012345678")
    s2 = AchtPuzzel("021345678")
    s3 = AchtPuzzel("042315678")
    s4 = AchtPuzzel("724506831")
    assert s1.manhattan_heuristiek(s2) == 2
    assert s1.manhattan_heuristiek(s3) == 2
    assert s1.manhattan_heuristiek(s4) == 18
    assert s4.manhattan_heuristiek(s1) == 18
    assert s2.manhattan_heuristiek(s2) == 0    

@pytest.mark.timeout(2)
def test_plan_lt(): 
    # test of __lt__ correct werkt
    p1 = Plan(toestand="s1", voorganger=None, actie=None, kost=0, h_waarde=100)
    assert not p1 < p1
    p2 = Plan(toestand="s2", voorganger=p1, actie=None, kost=50, h_waarde=75)
    assert p1 < p2
    assert p2 > p1
    assert not p2 < p1

@pytest.mark.timeout(2)
def test_plan_geef_actiesequentie():
    p1 = Plan(toestand="s1", voorganger=None, actie=None, kost=0, h_waarde=100)
    assert p1.geef_actie_sequentie() == []
    p2 = Plan(toestand="s2", voorganger=p1, actie="a1", kost=10, h_waarde=90)
    assert p2.geef_actie_sequentie() == ['a1']
    p3 = Plan(toestand="s3", voorganger=p2, actie="a2", kost=20, h_waarde=80)
    p4 = Plan(toestand="s4", voorganger=p3, actie="a3", kost=30, h_waarde=70)
    assert p4.geef_actie_sequentie() == ['a1','a2','a3']

# test zonder heuristiek op simpele puzzels.
@pytest.mark.timeout(4)
def test_plan_a_ster_zoeken_zonder_heuristiek():
    doelpuzzel = AchtPuzzel("123456780")
    is_doel = lambda puzzel : puzzel == doelpuzzel
    heuristiek = lambda toestand: 0

    startpuzzel1 = AchtPuzzel("123456708")
    startpuzzel2 = AchtPuzzel("123406758")

    assert a_ster_zoeken(startpuzzel1,is_doel,heuristiek) == (['R'],1)

    assert a_ster_zoeken(startpuzzel2,is_doel,heuristiek) == (['O','R'],2)

# met aantal verkeerd als heuristiek
@pytest.mark.timeout(3)
def test_plan_a_ster_zoeken_aantal_verkeerd_heuristiek():
    doelpuzzel = AchtPuzzel("123456780")
    is_doel = lambda puzzel : puzzel == doelpuzzel
    heuristiek = lambda toestand: toestand.aantal_verkeerd(doelpuzzel)

    startpuzzel1 = AchtPuzzel("123456708")
    startpuzzel2 = AchtPuzzel("123406758")
    startpuzzel3 = AchtPuzzel("012345678")


    assert a_ster_zoeken(startpuzzel1,is_doel,heuristiek) == (['R'],1)

    assert a_ster_zoeken(startpuzzel2,is_doel,heuristiek) == (['O','R'],2)

    assert a_ster_zoeken(startpuzzel3,is_doel,heuristiek) == (['O', 'R', 'R', 'B', 'L', 'L', 'O', 'O', 'R', 'B', 'B', 'R', 'O', 'L', 'L', 'B', 'R', 'R', 'O', 'L', 'O', 'R']
                                                              ,22)
    
# met manhattanafstand als heuristiek
@pytest.mark.timeout(3)
def test_plan_a_ster_zoeken_manhattan_heuristiek():
    doelpuzzel = AchtPuzzel("123456780")
    is_doel = lambda puzzel : puzzel == doelpuzzel
    heuristiek = lambda toestand: toestand.manhattan_heuristiek(doelpuzzel)

    startpuzzel1 = AchtPuzzel("123456708")
    startpuzzel2 = AchtPuzzel("123406758")
    startpuzzel3 = AchtPuzzel("012345678")

    assert a_ster_zoeken(startpuzzel1,is_doel,heuristiek) == (['R'],1)

    assert a_ster_zoeken(startpuzzel2,is_doel,heuristiek) == (['O','R'],2)

    assert a_ster_zoeken(startpuzzel3,is_doel,heuristiek) == (['O', 'R', 'R', 'B', 'L', 'L', 'O', 'O', 'R', 'B', 'B', 'R', 'O', 'L', 'L', 'B', 'R', 'R', 'O', 'L', 'O', 'R']
                                                              ,22)

@pytest.mark.timeout(5)
def test_plan_a_ster_zoeken_onoplosbaar():
    doelpuzzel = AchtPuzzel("123456780")
    is_doel = lambda puzzel : puzzel == doelpuzzel
    heuristiek = lambda toestand: toestand.manhattan_heuristiek(doelpuzzel)

    startpuzzel_onoplosbaar = AchtPuzzel("120456783")

    assert a_ster_zoeken(startpuzzel_onoplosbaar,is_doel,heuristiek) is None
