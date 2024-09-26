quest_name = input("Wprowadź nazwę questa: ")
quest_title = input("Wprowadź tytuł questa: ")
level_to_start = input("Od jakiego levela ma sie zaczynać misja : ")
num_lines = int(input("Ile linii tekstu chcesz wygenerować (1-4) ? "))
task_line = input("Wprowadź linię tekstu na pomarańczowo : ")
yang_reward = input("Ile yang dostaniesz za wykonanie misji : ")
exp_reward = input("Ile EXP dostaniesz za wykonanie misji : ")
mob_name = input("Wprowadź nazwę potwora do zabicia : ")
mob_id = input("Wprowadź ID potwora do zabicia : ")
mob_quantity = input("Ile mobów trzeba zabić w tej misji : ")
num_rewards = int(input("Ile nagród ma być w tej misji (1-5) : "))

with open(f"{quest_name}.txt", "w") as quest_file:
    quest_file.write(f"quest {quest_name} begin\n")
    quest_file.write("\tstate start begin\n")
    quest_file.write(f"\t\twhen login with pc.level >= {level_to_start} begin\n")
    quest_file.write("\t\t\tset_state(information)\n")
    quest_file.write("\t\tend\n")
    quest_file.write("\tend\n\n")

    quest_file.write("\tstate information begin\n")
    quest_file.write("\t\twhen letter begin\n")
    quest_file.write(f'\t\t\tsend_letter("{quest_title}")\n')
    quest_file.write("\t\tend\n\n")

    quest_file.write("\t\twhen info or button begin\n")
    quest_file.write(f'\t\t\tsay_title("{quest_title}")\n')

    for i in range(num_lines):
        line = input(f"Wprowadź linię tekstu {i + 1}: ")
        quest_file.write(f'\t\t\tsay("{line}")\n')

    quest_file.write(f'\t\t\tsay_reward("{task_line}")\n')
    quest_file.write("\t\t\tsay(\"\")\n")
    quest_file.write(f'\t\t\tpc.setqf("state", {mob_quantity})\n')
    quest_file.write(f'\t\t\tq.set_counter("{mob_name}", {mob_quantity})\n')
    quest_file.write("\t\tend\n\n")

    quest_file.write(f'\t\twhen {mob_id}.kill begin\n')
    quest_file.write("\t\t\tlocal count = pc.getqf(\"state\") - 1\n")
    quest_file.write(f"\t\t\tif count <= {mob_quantity} then\n")
    quest_file.write("\t\t\t\tpc.setqf(\"state\", count)\n")
    quest_file.write(f'\t\t\t\tq.set_counter("{mob_name}", count)\n')
    quest_file.write("\t\t\tend\n")
    quest_file.write("\t\t\tif count == 0 then\n")
    quest_file.write(f'\t\t\t\tsay_title("{quest_title} - Ukończono!")\n')
    quest_file.write("\t\t\t\tsay(\"\")\n")
    quest_file.write('\t\t\t\tsay("Ukończyłeś z powodzeniem misję!")\n')
    quest_file.write('\t\t\t\tsay("Oto kilka ciekawych nagród w zamian.")\n')
    quest_file.write('\t\t\t\tsay_reward("Nagrody:")\n')
    #REWARD TEXT
    for i in range(num_rewards):
        reward_text = input(f"Wprowadź nazwę nagrody o numerze {i + 1}: ")
        quest_file.write(f'\t\t\t\tsay_reward("Otrzymałeś {reward_text}")\n')

    quest_file.write(f'\t\t\t\tsay_reward("Otrzymałeś {yang_reward} Yang")\n')
    quest_file.write(f'\t\t\t\tsay_reward("Otrzymałeś {exp_reward} EXP.")\n')

    #HORSE REWARD
    horse_level_reward = input("Czy w tej misji ma być poziom konia jako nagroda? (True/False): ").lower() == 'true'

    if horse_level_reward:
        horse_level = input("Wprowadź poziom konia za tą misję: ")
        quest_file.write(f'\t\t\t\tsay_reward("Otrzymałeś poziom konia : {horse_level}!")\n')

    #METIN2 THINGS
    quest_file.write(f'\t\t\t\tpc.change_money({yang_reward})\n')
    quest_file.write(f'\t\t\t\tpc.give_exp2({exp_reward})\n')

    #REWARD ITEMS
    for i in range(num_rewards):
        item_id = input(f"Wprowadź ID itemu nagrody o numerze {i + 1}: ")
        quantity = input(f"Wprowadź ilość itemu nagrody o numerze {i + 1}: ")
        quest_file.write(f'\t\t\t\tpc.give_item2({item_id}, {quantity})\n')

    if horse_level_reward:
        quest_file.write(f'\t\t\t\thorse.set_level("{horse_level}")\n')

    quest_file.write(f'\t\t\t\tclear_letter()\n')
    quest_file.write(f'\t\t\t\tset_state(__COMPLETE__)\n')

    quest_file.write(f'\t\t\tend\n')
    quest_file.write(f'\t\tend\n')
    quest_file.write(f'\tend\n')
    quest_file.write(f'\n')

    quest_file.write(f'\tstate __COMPLETE__ begin\n')
    quest_file.write(f'\tend\n')
    quest_file.write(f'end\n')