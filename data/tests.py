def test_q1(fname, lname, age):
    assert fname is not None, "Please initialize `fname` list to store results."
    assert lname is not None, "Please initialize `lname` list to store results."
    assert age is not None, "Please initialize `age` list to store results."

    assert fname == ['Bellatrix', 'Albus', 'Harry', 'Molly', 'Cho'], '`fname` list not accurate.'
    assert lname == ['Lestrange', 'Dumbledore', 'Potter', 'Weaseley', 'Chang'], '`lname` list not accurate.'
    assert age == [47, 115, 29, 48, 28], '`age` list not accurate.'
    print("🎉 Successfully answered question! Please move on to the next question.")

def test_q2(list):
    import datetime
    assert list == [
        datetime.date(2021, 11, 29),
        datetime.date(2021, 11, 30), 
        datetime.date(2021, 11, 30), 
        datetime.date(2021, 12, 10), 
        datetime.date(2021, 12, 11), 
        datetime.date(2021, 12, 11), 
        datetime.date(2021, 12, 12), 
        datetime.date(2021, 12, 13), 
        datetime.date(2021, 12, 17), 
        datetime.date(2021, 12, 19), 
        datetime.date(2021, 12, 23), 
        datetime.date(2021, 12, 25), 
        datetime.date(2021, 12, 27), 
        datetime.date(2021, 12, 30), 
        datetime.date(2022, 1, 2), 
        datetime.date(2022, 1, 2), 
        datetime.date(2022, 1, 2), 
        datetime.date(2022, 1, 4), 
        datetime.date(2022, 1, 5), 
        datetime.date(2022, 1, 5), 
        datetime.date(2022, 1, 5), 
        datetime.date(2022, 1, 2), 
        datetime.date(2022, 1, 2), 
        datetime.date(2022, 1, 2), 
        datetime.date(2022, 1, 4), 
        datetime.date(2022, 1, 7)
        ], "Function did not return the expected output."
    print("🎉 Successfully answered question! Please move on to the next question.")

def test_q3(shop, products):
    assert shop and products is not None, "Please initialize `shop` and `products` variables to store results."
    assert shop == 303, "Shop ID was not correct."
    assert products == 33, "Number of 'Faulty' products was not correct."
    print("🎉 Successfully answered question! Please move on to the next question.")

def test_q4(td):
    import pandas as pd
    assert type(td) == pd.Timedelta, "Class of `td` was not pd.Timedelta."
    assert td == pd.Timedelta('5 days 15:10:47.976381821'), "Average delivery time did not return the expected output."
    print("🎉 Congratulations! You have completed the technical interview.")