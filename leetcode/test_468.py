from unittest.mock import patch

from leetcode.validate_ip_address import valid_ip4, valid_ip6, Solution


def test_main_runner():
    with patch('leetcode.validate_ip_address.valid_ip4', return_value=True):
        assert 'IPv4' == Solution().validIPAddress('hello')
    with patch('leetcode.validate_ip_address.valid_ip6', return_value=True):
        assert 'IPv6' == Solution().validIPAddress('hello')
    with patch('leetcode.validate_ip_address.valid_ip6', return_value=False):
        assert 'Neither' == Solution().validIPAddress('hello')


def test_ip4():
    assert not valid_ip4("1.0.1.")
    assert valid_ip4("172.16.254.1")
    assert not valid_ip4("0172.16.254.1")
    assert not valid_ip4("1.1.1.01")
    assert not valid_ip4("0x72.16.254.1")
    assert not valid_ip4("4444.16.254.1")
    assert not valid_ip4("4444.16.254")
    assert not valid_ip4("256.256.256.256")
    assert not valid_ip4("1e1.16.254.5555")

def test_ip6():
    assert valid_ip6('2001:0db8:85a3:0:0:8A2E:0370:7334')
    assert not valid_ip6('2001:0db8:85a3:0:0:8A2E:0370:7334:')

