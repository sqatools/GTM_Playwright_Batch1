"""
pytest fixture and marker
# Fixture scope

function scope :  pytest.fixture(scope='function')
               ->  function fixture will execute before and after execution of any test function.

class scope : pytest.fixture(scope='class')
               ->  class fixture will execute before and after execution of test class.

module scope : pytest.fixture(scope='module')
              -> module fixture will execute before and after execution of test module file.

package scope: pytest.fixture(scope='package')
              -> package fixture will execute before and after execution of package files execution.

session scope:  pytest.fixture(scope='session')
            ->  session fixture will execute before and after execution of all files in all packages.

"""
import pytest
from environment_data import *


@pytest.fixture(scope='function', autouse=True)
def fun_fix():
    """
     function fixture will execute before and after execution of any test function.
    :return:
    """
    print("\n----start func fixture-----")
    yield
    print("\n----end func fixture-----")

@pytest.fixture(scope='class', autouse=True)
def class_fixture():
    """
     class fixture will execute before and after execution of test class.
    :return:
    """
    print("\n----start class fixture-----")
    yield
    print("\n----end class fixture-----")

@pytest.fixture(scope='module', autouse=True)
def module_fixture():
    """
     package fixture will execute before and after execution of package files execution.
    :return:
    """
    print("\n----start module fixture-----")
    yield
    print("\n----end module fixture-----")


@pytest.fixture(scope='package', autouse=True)
def package_fixture():
    """
     module fixture will execute before and after execution of test module file.
    :return:
    """
    print("\n----package package fixture-----")
    yield
    print("\n----package package fixture-----")

@pytest.fixture(scope='session', autouse=True)
def session_fixture():
    """
     package fixture will execute before and after execution of package files execution.
    :return:
    """
    print("\n----start session fixture-----")
    yield
    print("\n----end session fixture-----")



class TestSmoke:
    ENV = "TEST"

    @pytest.mark.parametrize("username, password", [
        ('user1@gmail.com', 'user12345'),
        ('user2@gmail.com', 'admin1234'),
        ('user3@gmail.com', 'P@122344'),
        ('user4@gmail.com', 'P@ssw0rd'),
        ('user5@gmail.com', 'End@pass'),

    ])
    def test_login(self, username, password):
        if (username, password) in db_users_details:
            print("Login Successful")
        else:
            assert False, "Invalid Credentials"


    @pytest.mark.smoke
    def test_addition(self):
        n1 = 40
        n2 = 50
        assert n1+n2 == 90

    @pytest.mark.smoke
    def test_multiplication(self):
        n1 = 4
        n2 = 5
        assert n1*n2 == 20

    @pytest.mark.smoke
    @pytest.mark.sanity
    def test_division(self):
        n1 = 40
        n2 = 5
        assert n1//n2 == 8

    @pytest.mark.xfail
    @pytest.mark.sanity
    def test_subtraction(self):
        n1 = 40
        n2 = 5
        assert n1 - n2 == 33

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_addition_2(self):
        n1 = 40
        n2 = 50
        assert n1+n2 == 90

    @pytest.mark.regression
    def test_multiplication_2(self):
        n1 = 4
        n2 = 5
        assert n1*n2 == 20

    @pytest.mark.skip  # This is unconditional skip
    @pytest.mark.xfail
    @pytest.mark.nonfunc
    def test_division_2(self):
        n1 = 40
        n2 = 5
        assert n1//n2 == 8

    @pytest.mark.skipif(ENV != "TEST", reason="This feature in only available in test env")
    @pytest.mark.nonfunc
    def test_subtraction_2(self):
        n1 = 40
        n2 = 5
        assert n1 - n2 == 33









