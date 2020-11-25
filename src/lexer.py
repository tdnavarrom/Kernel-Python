status = {
    'OK': 'OK',
    'BAD': 'Err',
}

rule_argument_syntaxis = {
    'exit': 1,
    'help': 1,
    'create_dir': 2,
    'rm_dir': 2
}

def check_sintaxis(rule):
    if rule.split(' ')[0] in rule_argument_syntaxis:
        parameters = rule.split(' ')
        raw_rule = parameters[0]
        quantity_parameters = len(parameters)

        correct = rule_argument_syntaxis[raw_rule] == quantity_parameters
        if correct:
            return status['OK']
    else:
        return status['BAD']