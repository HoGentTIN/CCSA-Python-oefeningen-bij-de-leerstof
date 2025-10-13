import pytest

from h3_hashtabellen.twee_som import two_sum, two_sum_hash

CASES = [
    # doel = 10
    ([1, 4, 5, 7, 8, 9], 10, (0, 5)),
    # doel = 20
    ([1, 5, 16, 17, 18, 20, 21, 22, 23, 24, 25, 26, 19], 20, (0, 12)),
    # doel = 50 (met 49 als laatste in lijst → eerste geldige paar op indices 0 en 25)
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
      21, 22, 23, 24, 25, 49], 50, (0, 25)),
    # doel = 50 (zelfde set maar met '1' op het einde → eerste geldige paar op indices 24 en 25)
    ([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
      22, 23, 24, 25, 49, 1], 50, (24, 25)),
    # geen oplossing
    ([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
      22, 23, 24, 25, 49], 50, None),
]

@pytest.mark.timeout(1)
@pytest.mark.parametrize("getallen, doel, verwachte_returnwaarde", CASES,
                         ids=["10-ok","20-ok","50-front","50-tail","50-none"])
def test_two_sum(getallen, doel, verwachte_returnwaarde):
    assert two_sum(getallen, doel) == verwachte_returnwaarde

@pytest.mark.timeout(1)
@pytest.mark.parametrize("getallen, doel, verwachte_returnwaarde", CASES,
                         ids=["10-ok","20-ok","50-front","50-tail","50-none"])
def test_two_sum_hash(getallen, doel, verwachte_returnwaarde):
    assert two_sum_hash(getallen, doel) == verwachte_returnwaarde



# zeer lange lijst --> two_sum_hash zou sneller moeten zijn, maar in de praktijk is dat niet zo
# @pytest.mark.timeout(10)
# def test_two_sum_zeer_lange_lijst():
#     getallen = [i for i in range(50_000_000)] + [100_000_000]
#     doel = 100_000_000
#     verwachte_returnwaarde = (0, 50_000_000)
#     assert two_sum(getallen, doel) == verwachte_returnwaarde

# @pytest.mark.timeout(10)
# def test_two_sum_hash_zeer_lange_lijst():
#     getallen = [i for i in range(50_000_000)] + [100_000_000]
#     doel = 100_000_000
#     verwachte_returnwaarde = (0, 50_000_000)
#     assert two_sum_hash(getallen, doel) == verwachte_returnwaarde