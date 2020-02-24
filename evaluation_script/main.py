import random


def evaluate(test_annotation_file, user_submission_file, phase_codename, **kwargs):
    print("Starting Evaluation.....")
    """
    Evaluates the submission for a particular challenge phase adn returns score
    Arguments:

        `test_annotations_file`: Path to test_annotation_file on the server
        `user_submission_file`: Path to file submitted by the user
        `phase_codename`: Phase to which submission is made

        `**kwargs`: keyword arguments that contains additional submission
        metadata that challenge hosts can use to send slack notification.
        You can access the submission metadata
        with kwargs['submission_metadata']

        Example: A sample submission metadata can be accessed like this:
        >>> print(kwargs['submission_metadata'])
        {
            'status': u'running',
            'when_made_public': None,
            'participant_team': 5,
            'input_file': 'https://abc.xyz/path/to/submission/file.json',
            'execution_time': u'123',
            'publication_url': u'ABC',
            'challenge_phase': 1,
            'created_by': u'ABC',
            'stdout_file': 'https://abc.xyz/path/to/stdout/file.json',
            'method_name': u'Test',
            'stderr_file': 'https://abc.xyz/path/to/stderr/file.json',
            'participant_team_name': u'Test Team',
            'project_url': u'http://foo.bar',
            'method_description': u'ABC',
            'is_public': False,
            'submission_result_file': 'https://abc.xyz/path/result/file.json',
            'id': 123,
            'submitted_at': u'2017-03-20T19:22:03.880652Z'
        }
    """

    print("*** Arguments ***")
    print("test_annotation_file: ", test_annotation_file)
    print("user_submission_file: ", user_submission_file)
    print("phase_codename: ", phase_codename)
    print(kwargs['submission_metadata'])
    print("")

    output = {}
    if phase_codename == "dev-groundtruth":
        print("Evaluating for dev-groundtruth")

    elif phase_codename == "dev-perception":
        print("Evaluating for dev-perception")

    elif phase_codename == "competition-groundtruth":
        print("Evaluating for competition-groundtruth")

    elif phase_codename == "competition-perception":
        print("Evaluating for competition-perception")


    # Roll the dice!
    recall = random.random()
    precision = random.random()
    collisions = random.random()
    actions = random.random()

    print("Completed evaluation.")

    output["result"] = [
        {
            "withheld_scenes": {
                "Recall": recall,
                "Precision": precision,
                "Collisions": collisions,
                "Actions": actions,
                "Weighted Total": recall + 0.1*precision - 0.1*collisions - 0.1*actions
            }
        }
    ]

    # To display the results in the result file
    output["submission_result"] = output["result"][0]["withheld_scenes"]
    return output
