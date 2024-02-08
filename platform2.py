# User Platform and Problem Component Script with Loop and Exit

part_list = {
    'gcm': 'Escalate to CNE-Gateway team | Phone 884140 (Primary) or 884141 (Secondary).',
    'rfgw': 'Escalate to DETOPS team | Phone 286322 (Primary) or 286281 (Secondary).',
    'idm': 'Escalate to CNE-Gateway team | Phone 884140 (Primary) or 884141 (Secondary).',
    'idc': 'Escalate to CNE-Gateway team | Phone 884140 (Primary) or 884141 (Secondary).',
    'igm': 'Escalate to CNE-Gateway team | Phone 884140 (Primary) or 884141 (Secondary).',
    'ipgw': 'Escalate to CNE-Gateway team | Phone 884140 (Primary) or 884141 (Secondary).',
    'tds': 'Escalate to SDG-Gateway team | Phone 884140 (Primary) or 884141 (Secondary).',
    'igw': 'Escalate to SDG-Gateway team | Phone 884140 (Primary) or 884141 (Secondary).',
    'omm': 'Escalate to SDG-Gateway team | Phone 884140 (Primary) or 884141 (Secondary).',
    'cro': 'Escalate to SDG-Gateway team | Phone 884140 (Primary) or 884141 (Secondary).',
    'sgw': 'Escalate to SDG-Gateway team | Phone 884140 (Primary) or 884141 (Secondary).',
}

def get_platform():
    platforms = ['ku', 'j1', 'j2', 'j3']
    platform = input(f"Select a user platform ({', '.join(platforms)}) or type 'exit' to end: ").lower()
    
    while platform != 'exit' and platform not in platforms:
        print("\nInvalid platform. Please select ku, j1, j2, j3, or type 'exit' to end.\n")
        platform = input(f"Select a user platform ({', '.join(platforms)}) or type 'exit' to end: ").lower()

    return platform

def get_problem_component():
    return input("\nWhat is the problem component? Type 'exit' to end: ").lower()

def escalate_to_team(component):
    if component != 'exit' and component.lower() in part_list:
        return part_list[component.lower()]
    elif component == 'exit':
        return "Exiting the script."
    else:
        return "\nProblem component not found in the list."

def main():
    while True:
        # Get user platform
        user_platform = get_platform()

        if user_platform == 'exit':
            print("Exiting.")
            break

        # Get problem component
        problem_component = get_problem_component()

        if problem_component == 'exit':
            print("Exiting.")
            break

        # Escalate to the team based on the problem component
        escalation_info = escalate_to_team(problem_component)

        # Display the result
        print(f"\nUser platform selected: {user_platform}")
        print(f"\nProblem component identified: {problem_component}")
        print(f"\nEscalation information: {escalation_info}\n")

if __name__ == "__main__":
    main()
