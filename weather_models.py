from collections import namedtuple

Gaussian = namedtuple('Gaussian', ['mean', 'var', 'adjust'])
WeatherModel = namedtuple('WeatherModel', ['condition_weights', 'temperature', 'pressure', 'humidity'])


WEATHER_MODELS = {
    'SYD': WeatherModel([0.1, 0.4, 0, 0.5],
                        [
                            Gaussian(26, 6, [-4, -6, 0, 4]),
                            Gaussian(25, 5, [-4, -6, 0, 4]),
                            Gaussian(24, 4, [-4, -6, 0, 4]),
                            Gaussian(22, 4, [-4, -6, 0, 4]),
                            Gaussian(19, 5, [-4, -6, 0, 4]),
                            Gaussian(17, 4, [-4, -6, 0, 4]),
                            Gaussian(16, 4, [-4, -6, 0, 4]),
                            Gaussian(17, 5, [-4, -6, 0, 4]),
                            Gaussian(20, 5, [-4, -6, 0, 4]),
                            Gaussian(22, 6, [-4, -6, 0, 4]),
                            Gaussian(23, 6, [-4, -6, 0, 4]),
                            Gaussian(25, 6, [-4, -6, 0, 4]),
                        ],
                        [
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                        ],
                        [
                            Gaussian(71, 5, [10, 20, 0, -20]),
                            Gaussian(74, 5, [10, 20, 0, -20]),
                            Gaussian(74, 5, [10, 20, 0, -20]),
                            Gaussian(72, 5, [10, 20, 0, -20]),
                            Gaussian(74, 5, [10, 20, 0, -20]),
                            Gaussian(74, 5, [10, 20, 0, -20]),
                            Gaussian(71, 5, [10, 20, 0, -20]),
                            Gaussian(66, 5, [10, 20, 0, -20]),
                            Gaussian(62, 5, [10, 20, 0, -20]),
                            Gaussian(61, 5, [10, 20, 0, -20]),
                            Gaussian(66, 5, [10, 20, 0, -20]),
                            Gaussian(67, 5, [10, 20, 0, -20]),
                        ]
                        ),

    'MEL': WeatherModel([0.1, 0.4, 0, 0.5],
                        [
                            Gaussian(26, 6, [-4, -6, 0, 4]),
                            Gaussian(25, 5, [-4, -6, 0, 4]),
                            Gaussian(24, 4, [-4, -6, 0, 4]),
                            Gaussian(22, 4, [-4, -6, 0, 4]),
                            Gaussian(19, 5, [-4, -6, 0, 4]),
                            Gaussian(17, 4, [-4, -6, 0, 4]),
                            Gaussian(16, 4, [-4, -6, 0, 4]),
                            Gaussian(17, 5, [-4, -6, 0, 4]),
                            Gaussian(20, 5, [-4, -6, 0, 4]),
                            Gaussian(22, 6, [-4, -6, 0, 4]),
                            Gaussian(23, 6, [-4, -6, 0, 4]),
                            Gaussian(25, 6, [-4, -6, 0, 4]),
                        ],
                        [
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                        ],
                        [
                            Gaussian(71, 5, [10, 20, 0, -20]),
                            Gaussian(74, 5, [10, 20, 0, -20]),
                            Gaussian(74, 5, [10, 20, 0, -20]),
                            Gaussian(72, 5, [10, 20, 0, -20]),
                            Gaussian(74, 5, [10, 20, 0, -20]),
                            Gaussian(74, 5, [10, 20, 0, -20]),
                            Gaussian(71, 5, [10, 20, 0, -20]),
                            Gaussian(66, 5, [10, 20, 0, -20]),
                            Gaussian(62, 5, [10, 20, 0, -20]),
                            Gaussian(61, 5, [10, 20, 0, -20]),
                            Gaussian(66, 5, [10, 20, 0, -20]),
                            Gaussian(67, 5, [10, 20, 0, -20]),
                        ]
                        ),

    'ADL': WeatherModel([0.1, 0.4, 0, 0.5],
                        [
                            Gaussian(26, 6, [-4, -6, 0, 4]),
                            Gaussian(25, 5, [-4, -6, 0, 4]),
                            Gaussian(24, 4, [-4, -6, 0, 4]),
                            Gaussian(22, 4, [-4, -6, 0, 4]),
                            Gaussian(19, 5, [-4, -6, 0, 4]),
                            Gaussian(17, 4, [-4, -6, 0, 4]),
                            Gaussian(16, 4, [-4, -6, 0, 4]),
                            Gaussian(17, 5, [-4, -6, 0, 4]),
                            Gaussian(20, 5, [-4, -6, 0, 4]),
                            Gaussian(22, 6, [-4, -6, 0, 4]),
                            Gaussian(23, 6, [-4, -6, 0, 4]),
                            Gaussian(25, 6, [-4, -6, 0, 4]),
                        ],
                        [
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                        ],
                        [
                            Gaussian(71, 5, [10, 20, 0, -20]),
                            Gaussian(74, 5, [10, 20, 0, -20]),
                            Gaussian(74, 5, [10, 20, 0, -20]),
                            Gaussian(72, 5, [10, 20, 0, -20]),
                            Gaussian(74, 5, [10, 20, 0, -20]),
                            Gaussian(74, 5, [10, 20, 0, -20]),
                            Gaussian(71, 5, [10, 20, 0, -20]),
                            Gaussian(66, 5, [10, 20, 0, -20]),
                            Gaussian(62, 5, [10, 20, 0, -20]),
                            Gaussian(61, 5, [10, 20, 0, -20]),
                            Gaussian(66, 5, [10, 20, 0, -20]),
                            Gaussian(67, 5, [10, 20, 0, -20]),
                        ]
                        ),

    'PER': WeatherModel([0.1, 0.4, 0, 0.5],
                        [
                            Gaussian(26, 6, [-4, -6, 0, 4]),
                            Gaussian(25, 5, [-4, -6, 0, 4]),
                            Gaussian(24, 4, [-4, -6, 0, 4]),
                            Gaussian(22, 4, [-4, -6, 0, 4]),
                            Gaussian(19, 5, [-4, -6, 0, 4]),
                            Gaussian(17, 4, [-4, -6, 0, 4]),
                            Gaussian(16, 4, [-4, -6, 0, 4]),
                            Gaussian(17, 5, [-4, -6, 0, 4]),
                            Gaussian(20, 5, [-4, -6, 0, 4]),
                            Gaussian(22, 6, [-4, -6, 0, 4]),
                            Gaussian(23, 6, [-4, -6, 0, 4]),
                            Gaussian(25, 6, [-4, -6, 0, 4]),
                        ],
                        [
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                        ],
                        [
                            Gaussian(71, 5, [10, 20, 0, -20]),
                            Gaussian(74, 5, [10, 20, 0, -20]),
                            Gaussian(74, 5, [10, 20, 0, -20]),
                            Gaussian(72, 5, [10, 20, 0, -20]),
                            Gaussian(74, 5, [10, 20, 0, -20]),
                            Gaussian(74, 5, [10, 20, 0, -20]),
                            Gaussian(71, 5, [10, 20, 0, -20]),
                            Gaussian(66, 5, [10, 20, 0, -20]),
                            Gaussian(62, 5, [10, 20, 0, -20]),
                            Gaussian(61, 5, [10, 20, 0, -20]),
                            Gaussian(66, 5, [10, 20, 0, -20]),
                            Gaussian(67, 5, [10, 20, 0, -20]),
                        ]
                        ),

    'BLR': WeatherModel([0.1, 0.4, 0, 0.5],
                        [
                            Gaussian(26, 6, [-4, -6, 0, 4]),
                            Gaussian(25, 5, [-4, -6, 0, 4]),
                            Gaussian(24, 4, [-4, -6, 0, 4]),
                            Gaussian(22, 4, [-4, -6, 0, 4]),
                            Gaussian(19, 5, [-4, -6, 0, 4]),
                            Gaussian(17, 4, [-4, -6, 0, 4]),
                            Gaussian(16, 4, [-4, -6, 0, 4]),
                            Gaussian(17, 5, [-4, -6, 0, 4]),
                            Gaussian(20, 5, [-4, -6, 0, 4]),
                            Gaussian(22, 6, [-4, -6, 0, 4]),
                            Gaussian(23, 6, [-4, -6, 0, 4]),
                            Gaussian(25, 6, [-4, -6, 0, 4]),
                        ],
                        [
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                        ],
                        [
                            Gaussian(71, 5, [10, 20, 0, -20]),
                            Gaussian(74, 5, [10, 20, 0, -20]),
                            Gaussian(74, 5, [10, 20, 0, -20]),
                            Gaussian(72, 5, [10, 20, 0, -20]),
                            Gaussian(74, 5, [10, 20, 0, -20]),
                            Gaussian(74, 5, [10, 20, 0, -20]),
                            Gaussian(71, 5, [10, 20, 0, -20]),
                            Gaussian(66, 5, [10, 20, 0, -20]),
                            Gaussian(62, 5, [10, 20, 0, -20]),
                            Gaussian(61, 5, [10, 20, 0, -20]),
                            Gaussian(66, 5, [10, 20, 0, -20]),
                            Gaussian(67, 5, [10, 20, 0, -20]),
                        ]
                        ),

    'DEL': WeatherModel([0.1, 0.4, 0, 0.5],
                        [
                            Gaussian(26, 6, [-4, -6, 0, 4]),
                            Gaussian(25, 5, [-4, -6, 0, 4]),
                            Gaussian(24, 4, [-4, -6, 0, 4]),
                            Gaussian(22, 4, [-4, -6, 0, 4]),
                            Gaussian(19, 5, [-4, -6, 0, 4]),
                            Gaussian(17, 4, [-4, -6, 0, 4]),
                            Gaussian(16, 4, [-4, -6, 0, 4]),
                            Gaussian(17, 5, [-4, -6, 0, 4]),
                            Gaussian(20, 5, [-4, -6, 0, 4]),
                            Gaussian(22, 6, [-4, -6, 0, 4]),
                            Gaussian(23, 6, [-4, -6, 0, 4]),
                            Gaussian(25, 6, [-4, -6, 0, 4]),
                        ],
                        [
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                        ],
                        [
                            Gaussian(71, 5, [10, 20, 0, -20]),
                            Gaussian(74, 5, [10, 20, 0, -20]),
                            Gaussian(74, 5, [10, 20, 0, -20]),
                            Gaussian(72, 5, [10, 20, 0, -20]),
                            Gaussian(74, 5, [10, 20, 0, -20]),
                            Gaussian(74, 5, [10, 20, 0, -20]),
                            Gaussian(71, 5, [10, 20, 0, -20]),
                            Gaussian(66, 5, [10, 20, 0, -20]),
                            Gaussian(62, 5, [10, 20, 0, -20]),
                            Gaussian(61, 5, [10, 20, 0, -20]),
                            Gaussian(66, 5, [10, 20, 0, -20]),
                            Gaussian(67, 5, [10, 20, 0, -20]),
                        ]
                        ),

    'HYD': WeatherModel([0.1, 0.4, 0, 0.5],
                        [
                            Gaussian(26, 6, [-4, -6, 0, 4]),
                            Gaussian(25, 5, [-4, -6, 0, 4]),
                            Gaussian(24, 4, [-4, -6, 0, 4]),
                            Gaussian(22, 4, [-4, -6, 0, 4]),
                            Gaussian(19, 5, [-4, -6, 0, 4]),
                            Gaussian(17, 4, [-4, -6, 0, 4]),
                            Gaussian(16, 4, [-4, -6, 0, 4]),
                            Gaussian(17, 5, [-4, -6, 0, 4]),
                            Gaussian(20, 5, [-4, -6, 0, 4]),
                            Gaussian(22, 6, [-4, -6, 0, 4]),
                            Gaussian(23, 6, [-4, -6, 0, 4]),
                            Gaussian(25, 6, [-4, -6, 0, 4]),
                        ],
                        [
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                        ],
                        [
                            Gaussian(71, 5, [10, 20, 0, -20]),
                            Gaussian(74, 5, [10, 20, 0, -20]),
                            Gaussian(74, 5, [10, 20, 0, -20]),
                            Gaussian(72, 5, [10, 20, 0, -20]),
                            Gaussian(74, 5, [10, 20, 0, -20]),
                            Gaussian(74, 5, [10, 20, 0, -20]),
                            Gaussian(71, 5, [10, 20, 0, -20]),
                            Gaussian(66, 5, [10, 20, 0, -20]),
                            Gaussian(62, 5, [10, 20, 0, -20]),
                            Gaussian(61, 5, [10, 20, 0, -20]),
                            Gaussian(66, 5, [10, 20, 0, -20]),
                            Gaussian(67, 5, [10, 20, 0, -20]),
                        ]
                        ),

    'SFO': WeatherModel([0.1, 0.4, 0, 0.5],
                        [
                            Gaussian(26, 6, [-4, -6, 0, 4]),
                            Gaussian(25, 5, [-4, -6, 0, 4]),
                            Gaussian(24, 4, [-4, -6, 0, 4]),
                            Gaussian(22, 4, [-4, -6, 0, 4]),
                            Gaussian(19, 5, [-4, -6, 0, 4]),
                            Gaussian(17, 4, [-4, -6, 0, 4]),
                            Gaussian(16, 4, [-4, -6, 0, 4]),
                            Gaussian(17, 5, [-4, -6, 0, 4]),
                            Gaussian(20, 5, [-4, -6, 0, 4]),
                            Gaussian(22, 6, [-4, -6, 0, 4]),
                            Gaussian(23, 6, [-4, -6, 0, 4]),
                            Gaussian(25, 6, [-4, -6, 0, 4]),
                        ],
                        [
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                        ],
                        [
                            Gaussian(71, 5, [10, 20, 0, -20]),
                            Gaussian(74, 5, [10, 20, 0, -20]),
                            Gaussian(74, 5, [10, 20, 0, -20]),
                            Gaussian(72, 5, [10, 20, 0, -20]),
                            Gaussian(74, 5, [10, 20, 0, -20]),
                            Gaussian(74, 5, [10, 20, 0, -20]),
                            Gaussian(71, 5, [10, 20, 0, -20]),
                            Gaussian(66, 5, [10, 20, 0, -20]),
                            Gaussian(62, 5, [10, 20, 0, -20]),
                            Gaussian(61, 5, [10, 20, 0, -20]),
                            Gaussian(66, 5, [10, 20, 0, -20]),
                            Gaussian(67, 5, [10, 20, 0, -20]),
                        ]
                        ),

    'JFK': WeatherModel([0.1, 0.4, 0, 0.5],
                        [
                            Gaussian(26, 6, [-4, -6, 0, 4]),
                            Gaussian(25, 5, [-4, -6, 0, 4]),
                            Gaussian(24, 4, [-4, -6, 0, 4]),
                            Gaussian(22, 4, [-4, -6, 0, 4]),
                            Gaussian(19, 5, [-4, -6, 0, 4]),
                            Gaussian(17, 4, [-4, -6, 0, 4]),
                            Gaussian(16, 4, [-4, -6, 0, 4]),
                            Gaussian(17, 5, [-4, -6, 0, 4]),
                            Gaussian(20, 5, [-4, -6, 0, 4]),
                            Gaussian(22, 6, [-4, -6, 0, 4]),
                            Gaussian(23, 6, [-4, -6, 0, 4]),
                            Gaussian(25, 6, [-4, -6, 0, 4]),
                        ],
                        [
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                        ],
                        [
                            Gaussian(71, 5, [10, 20, 0, -20]),
                            Gaussian(74, 5, [10, 20, 0, -20]),
                            Gaussian(74, 5, [10, 20, 0, -20]),
                            Gaussian(72, 5, [10, 20, 0, -20]),
                            Gaussian(74, 5, [10, 20, 0, -20]),
                            Gaussian(74, 5, [10, 20, 0, -20]),
                            Gaussian(71, 5, [10, 20, 0, -20]),
                            Gaussian(66, 5, [10, 20, 0, -20]),
                            Gaussian(62, 5, [10, 20, 0, -20]),
                            Gaussian(61, 5, [10, 20, 0, -20]),
                            Gaussian(66, 5, [10, 20, 0, -20]),
                            Gaussian(67, 5, [10, 20, 0, -20]),
                        ]
                        ),

    'ORD': WeatherModel([0.1, 0.4, 0, 0.5],
                        [
                            Gaussian(26, 6, [-4, -6, 0, 4]),
                            Gaussian(25, 5, [-4, -6, 0, 4]),
                            Gaussian(24, 4, [-4, -6, 0, 4]),
                            Gaussian(22, 4, [-4, -6, 0, 4]),
                            Gaussian(19, 5, [-4, -6, 0, 4]),
                            Gaussian(17, 4, [-4, -6, 0, 4]),
                            Gaussian(16, 4, [-4, -6, 0, 4]),
                            Gaussian(17, 5, [-4, -6, 0, 4]),
                            Gaussian(20, 5, [-4, -6, 0, 4]),
                            Gaussian(22, 6, [-4, -6, 0, 4]),
                            Gaussian(23, 6, [-4, -6, 0, 4]),
                            Gaussian(25, 6, [-4, -6, 0, 4]),
                        ],
                        [
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                            Gaussian(1010, 2, [-4, -6, 0, 20]),
                        ],
                        [
                            Gaussian(71, 5, [10, 20, 0, -20]),
                            Gaussian(74, 5, [10, 20, 0, -20]),
                            Gaussian(74, 5, [10, 20, 0, -20]),
                            Gaussian(72, 5, [10, 20, 0, -20]),
                            Gaussian(74, 5, [10, 20, 0, -20]),
                            Gaussian(74, 5, [10, 20, 0, -20]),
                            Gaussian(71, 5, [10, 20, 0, -20]),
                            Gaussian(66, 5, [10, 20, 0, -20]),
                            Gaussian(62, 5, [10, 20, 0, -20]),
                            Gaussian(61, 5, [10, 20, 0, -20]),
                            Gaussian(66, 5, [10, 20, 0, -20]),
                            Gaussian(67, 5, [10, 20, 0, -20]),
                        ]
                        ),
}