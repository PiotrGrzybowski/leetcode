def climb_stairs(stairs: int) -> int:
    """Solves stairs problem."""
    if stairs == 1:
        return 1
    elif stairs == 2:
        return 2
    else:
        last = 2
        earlier = 1
        answer = 0
        while stairs > 2:
            answer = earlier + last
            earlier = last
            last = answer
            stairs -= 1
        return answer


if __name__ == '__main__':
    assert climb_stairs(2) == 2
    assert climb_stairs(3) == 3
    assert climb_stairs(8) == 34
    assert climb_stairs(16) == 1597
