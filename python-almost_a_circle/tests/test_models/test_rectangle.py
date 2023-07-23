#tringIO()) as str_out:
            new.update(10, 10, 10, 10, 10)
            print(new)
            self.assertEqual(str_out.getvalue().strip(), res)

    def test_update_kwargs(self):
        """ Test update method with kwargs """
        new = Rectangle(1, 1)
        res = "[Rectangle] (1) 10/10 - 10/10"
        with patch('sys.stdout', new=StringIO()) as str_out:
            new.update(x=10, y=10, width=10, height=10, id=10)
            print(new)
            self.assertEqual(str_out.getvalue().strip(), res)

    def test_update_no_args(self):
        """ Test update method with no args """
        new = Rectangle(1, 1)
        res = "[Rectangle] (1) 1/1 - 1/1"
        with patch('sys.stdout', new=StringIO()) as str_out:
            new.update()
            print(new)
            self.assertEqual(str_out.getvalue().strip(), res)

    def test_update_args_after_kwargs(self):
        """ Test update method with args after kwargs """
        new = Rectangle(1, 1)
        res = "[Rectangle] (1) 1/1 - 1/1"
        with patch('sys.stdout', new=StringIO()) as str_out:
            new.update(x=10, y=10)
            new.update(1)
            print(new)
            self.assertEqual(str_out.getvalue().strip(), res)

    def test_update_kwargs_after_args(self):
        """ Test update method with kwargs after args """
        new = Rectangle(1, 1)
        res = "[Rectangle] (1) 1/1 - 1/1"
        with patch('sys.stdout', new=StringIO()) as str_out:
            new.update(1)
            new.update(x=10, y=10)
            print(new)
            self.assertEqual(str_out.getvalue().strip(), res)

    def test_to_dict(self):
        """ Test to_dictionary method """
        new = Rectangle(10, 2, 1, 9)
        res = {'x': 1, 'y': 9, 'width': 10, 'height': 2, 'id': 1}
        self.assertEqual(new.to_dictionary(), res)

    def test_save_to_file_none(self):
        """ Test save_to_file with None """
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_empty(self):
        """ Test save_to_file with empty list """
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_rectangles(self):
        """ Test save_to_file with list of rectangles """
        r1 = Rectangle(1, 1)
        r2 = Rectangle(2, 2)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            self.assertIn("id", file.read())

    def test_load_from_file_none(self):
        """ Test load_from_file with None """
        list_objs = Rectangle.load_from_file()
        self.assertEqual(list_objs, [])

    def test_load_from_file_empty(self):
        """ Test load_from_file with empty file """
        open("Rectangle.json", "w").close()
        list_objs = Rectangle.load_from_file()
        self.assertEqual(list_objs, [])

    def test_load_from_file_rectangles(self):
        """ Test load_from_file with rectangles """
        r1 = Rectangle(1, 1)
        r2 = Rectangle(2, 2)
        Rectangle.save_to_file([r1, r2])
        list_objs = Rectangle.load_from_file()
        self.assertEqual(len(list_objs), 2)

if __name__ == '__main__':
    unittest.main()
