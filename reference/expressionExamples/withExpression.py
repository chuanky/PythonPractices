import traceback

def test_with_expression():
    try:
        with open('test.txt', 'rm') as f:
            print(f.read())
    except:
        traceback.print_exc()

test_with_expression()