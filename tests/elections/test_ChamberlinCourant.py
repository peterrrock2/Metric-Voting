import numpy as np
from metric_voting import ChamberlinCourant, Borda
from metric_voting import uniform_profile


def test_basic_profile(basic_profile):
    E = ChamberlinCourant()
    assert set(E.elect(basic_profile, 1).tolist()) == {0}
    assert set(E.elect(basic_profile, 2).tolist()) == {1,3}
    assert set(E.elect(basic_profile, 3).tolist()) == {1,2,3}
    assert set(E.elect(basic_profile, 4).tolist()) == {0, 1, 2, 3}
    

def test_with_borda():
    E1 = ChamberlinCourant()
    E2 = Borda()
    profile = uniform_profile(200, 10)
    assert set(E1.elect(profile, 1).tolist()) == set(E2.elect(profile, 1).tolist()) 
    
    
def test_num_winners():
    E = ChamberlinCourant()
    for _ in range(10):
        profile = uniform_profile(200, 10)
        rand_k = np.random.randint(1, 10 + 1)
        assert len(E.elect(profile, rand_k)) == rand_k
        