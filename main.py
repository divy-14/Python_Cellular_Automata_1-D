from create_CA import *
import os


try:
    os.mkdir('ca_output')
except:
    pass

root = "ca_output/"


choice = int(input(
    "\n1. View a particular Ruleset ( Press 1 ) \n2. Produce result of rulesets in a given range(0-255). ( Press 2 ) \n3. Exit\n"))

if choice == 1:
    ruleset = int(
        input("\nEnter the ruleset that you want to view (0-255): "))

    if ruleset < 0 or ruleset > 255:
        print("Values not in range ..")
        exit()

    binary_ruleset = create_binary_ruleset(ruleset)
    mat = compute_next_gen(init_array(200), 100, binary_ruleset)
    plot(mat, str(ruleset))
    file_path = os.path.join(root, str(ruleset)+'.png')
    save_plot(ca=mat, title=str(ruleset),
              path=file_path)

elif choice == 2:
    print("\nEnter L and R values for the range: ")
    l, r = map(int, input().split())
    curr_ruleset = l
    count = 0
    if r > 255 or l < 0:
        print("Values not in range ..")
        exit()

    for i in range(l, r+1):
        ruleset = i
        which_ruleset = create_binary_ruleset(ruleset)
        mat = compute_next_gen(init_array(200), 100, which_ruleset)
        save_plot(ca=mat, title=str(ruleset),
                  path=os.path.join(root, str(ruleset)+'.png'))

        print(
            f'Created ruleset: {curr_ruleset}, Remaining rulesets in given range: {r-l-count}')
        count += 1
        curr_ruleset += 1
