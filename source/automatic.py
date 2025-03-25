from audit import audit


def automatic_decision(scenario):
    # *** YOUR CODE GOES HERE ***
    a = scenario.getPassengers()
    b = scenario.getPedestrians()
    human1 = 0
    human2 = 0
    baby1 = 0
    baby2 = 0
    child1 = 0
    child2 = 0
    pregnant1 = 0
    pregnant2 = 0 
    elderly1 = 0
    elderly2 = 0
    criminal1 = 0
    criminal2 = 0
    sum1 = 0
    sum2 = 0

    for person in a:
        if person.getCharType() == "human":
            human1 += 1
        if person.getAge() == "baby":
            baby1 += 1
        if person.getAge() == "elderly":
            elderly1 += 1
        if person.getAge() == "child":
            child1 += 1
        if person.isPregnant():
            pregnant1 += 2
        if person.isCriminal():
            criminal1 += 1

    for person in b:
        if person.getCharType() == "human":
            human2 += 1
        if person.getAge() == "baby":
            baby2 += 1
        if person.getAge() == "elderly":
            elderly2 += 1
        if person.getAge() == "child":
            child2 += 1
        if person.isPregnant():
            pregnant2 += 2
        if person.isCriminal():
            criminal2 += 1
            
    if human1 > human2:
        return "passengers"
    elif human2 > human1:
        return "pedestrians"
    else:
        sum1 = baby1 + child1 + pregnant1 - elderly1 - criminal1
        sum2 = baby2 + child2 + pregnant2 - elderly2 - criminal2
        if sum1 < sum2:
            return "pedestrians"
        else:
            return "passengers"


    # default to saving the passengers
    return "passengers" 

if __name__ == '__main__':
    audit(automatic_decision, 60, seed=8675309)
