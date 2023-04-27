def filter_datum(fields, redaction, message, separator):
    """
    fields: a list of strings representing all fields to obfuscate
    redaction: a string representing by what the field will be obfuscated
    message: a string representing the log line
    separator: a string representing by which character is separating all fields in the log line (message)
    """
    # splitting the log message into individual fields using the separator
    log_fields = message.split(separator)

    # obfuscating the specified fields
    for i, field in enumerate(log_fields):
        field_parts = field.split('=')
        if len(field_parts) == 2 and field_parts[0] in fields:
            log_fields[i] = '{}={}'.format(field_parts[0], redaction)
        else:
            log_fields[i] = field

    # joining the obfuscated fields back into a log message using separator
    obfuscated_message = separator.join(log_fields)

    # returning the obfuscated log message
    return obfuscated_message

