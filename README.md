# SentiBoard - Readme Documentation

## A Brief Description

SentiBoard uses chat logs and facial recognition data to carefully analyze the user’s mood. It then changes the color of the keyboard LEDs to display how the user is feeling as he/she is using it. Warm colors like red, orange, and yellow represent heightened sense of feeling such as anger, annoyance, and disgust while cool colors like green, blue, and purple represent mood associated with relaxation and happiness.

## Getting Started

This project was made for YHack 2016, so the coding is still rather rough. SentiBoard uses Python, OpenCV, NLTK, and the Corsair API (specifically with [this wrapper](https://pypi.python.org/pypi/cue_sdk/). The current files have only been tested on a Windows 10 machine, but the image processing and NLP portions were written in Linux (Ubuntu 16.04), and should work with the appropriate distros.

### Prerequisites

* OpenCV 2.4.x (Latest is [2.4.13](http://opencv.org/downloads.html)) - Installation instructions can be found in OpenCV's extensive documentation
* [NLTK](http://www.nltk.org/) - We use the Movie Review Corpus in NLTK
* [Corsair API (CUE SDK)](http://www.corsair.com/en-us/support/downloads) with [python wrapper](https://pypi.python.org/pypi/cue_sdk/)

### Installing

A step by step series of examples that tell you have to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc



