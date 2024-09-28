ip = input().strip()

if ':' in ip:
    # Process as IPv6
    parts = ip.split(':')
    if '' in parts:
        empty_indices = [i for i, part in enumerate(parts) if part == '']
        first_empty = empty_indices[0]
        last_empty = empty_indices[-1]
        left = parts[:first_empty]
        right = parts[last_empty + 1:]
        num_zero_groups = 8 - (len(left) + len(right))
        expanded = left + ['0000'] * num_zero_groups + right
    else:
        expanded = parts

    full_str = ''.join([part.zfill(4).lower() for part in expanded])
    reversed_str = full_str[::-1]
    ptr = '.'.join(reversed_str) + '.ip6.arpa.'
else:
    # Process as IPv4
    parts = ip.split('.')
    reversed_parts = reversed(parts)
    ptr = '.'.join(reversed_parts) + '.in-addr.arpa.'

print(ptr)