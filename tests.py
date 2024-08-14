import data
import create_kit


# Функции
def positive_attempts(firstname):
    copied_data = data.kit.copy()
    copied_data["name"] = firstname
    response = create_kit.create_kit(copied_data)

    assert response.status_code == 201
    assert response.json()["name"] == firstname


def negative_attempts(firstname):
    copied_data = data.kit.copy()
    copied_data["name"] = firstname
    response = create_kit.create_kit(copied_data)

    assert response.status_code == 400


def super_negative(body):
    response = create_kit.create_kit(body)

    assert response.status_code == 400


def test1():  # passed
    positive_attempts("a")


def test2():  # passed
    positive_attempts("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
    bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
    cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcd\
    abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
    cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
    cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")


def test3():  # failed 201 != 400
    negative_attempts("")


def test4():  # failed 201 != 400
    negative_attempts("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
    bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
    cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
    abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc\
    dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")


def test5():  # passed
    positive_attempts("QWErty")


def test6():  # passed
    positive_attempts("Мария")


def test7():  # passed
    positive_attempts('"№%@","')


def test8():  # passed
    positive_attempts("Человек и КО")


def test9():  # passed
    positive_attempts("123")


def test10():  # failed 500 != 400
    kit = data.kit.copy()
    kit.pop("name")
    super_negative(kit)


def test11():  # failed 201 != 400 ({'name': 123 ...
    copied_data = data.kit
    copied_data["name"] = 123
    response = create_kit.create_kit(copied_data)
    assert response.status_code == 400
