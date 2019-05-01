test = {
    'name': '1.1',
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # It looks like you didn't define the "answers" variable.
                    >>> # Make sure you've run the cell and check for typos!
                    >>> 'answer' in vars()
                    True
                    """
                },
                {
                    'code': r"""
                    >>> # Make sure you've put your answer inside quotation marks
                    >>> Traceback (most recent call last):
                    >>> ...
                    >>> NameError: ...
                    False
                    """
                },
                {
                    'code': r"""
                    >>> # You're close! Check your spelling (we're not looking for the planet)
                    >>> answer == "Jupiter"
                    False
                    """
                },                
                {
                    'code': r"""
                    >>> # This is another doctest.
                    >>> # This will run if the previous doctest passed
                    >>> answer == "Jupyter"
                    True
                    """
                }
            ]
        }
    ]
}