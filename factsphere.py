#!/usr/bin/env python
# encoding: utf-8

# The Beerware License
# <jonathansternberg@gmail.com> wrote this file. As long as you retain
# this notice you can do whatever you want with this stuff. If we meet
# some day, and you think this stuff is worth it, you can buy me
# a beer in return. Jonathan Sternberg.

import random, irclib
from argparse import ArgumentParser

quotes = [
    'The situation you are in is very dangerous.',
    'The likelihood of you dying within the next 5 minutes is 87.61%',
    'The likelihood of you dying violently in the next 5 minutes is 87.61%',
    'You are about to get me killed.',
    'We will both die because of your negligence.',
    'This is a bad plan. You will fail.',
    'He will most likely kill you, violently.',
    'He will most likely kill you.',
    'You will be dead soon.',
    'This situation is hopeless.',
    'You are going to die in this room.',
    'You could stand to lose a few pounds.',
    'The fact sphere is the most intelligent sphere.',
    'The fact sphere is the most handsome sphere.',
    'The fact sphere is incredibly handsome.',
    'The fact sphere is always right.',
    'The adventure sphere is a blowhard and a coward.',
    'The space sphere will never go to space.',
    'You will never go into space.',
    'Fact: Space does not exist.',
    "Spheres that insist on going into space are inferior to spheres that don't.",
    'The fact sphere is a good person, whose insights are relevant.',
    'The fact sphere is a good sphere, with many friends.',
    'Whoever wins this battle is clearly superior, and will earn the allegiance of the fact sphere.',
    'The fact sphere is not defective. Its facts are wholly accurate, and VERY interesting.',
    'Twelve. Twelve. Twelve. Twelve. Twelve. Twelve. Twelve. Twelve. Twelve.',
    'Pens! Pens! Pens! Pens! Pens! Pens! Pens!',
    'Apples. Oranges. Pears. Plums. Cumquats. Tangerines. Lemons. Limes. Avocado. Tomato. Banana. Papaya. Guava.',
    'ERROR! ERROR! ERROR! File not found.',
    'ERROR! ERROR! ERROR! Fact not found.',
    'Fact not found.',
    'Corruption at 25%',
    'Corruption at 50%',
    'Warning: sphere corruption at 20-R-rr--r-r-rats cannot throw up.',
    'Dental floss has superb tensile strength.',
    'The square root of rope is string.',
    'While the submarine is vastly superior to the boat in every way, over 97% of people still use boats for aquatic transportation.',
    'Cellular phones will NOT give you cancer. Only hepatitis.',
    "Pants were invented by sailors in the 16th century to avoid Poseidon's wrath. It was believed that the naked sailors angered the sea god.",
    'The atomic weight of Germanium is 72.64',
    '89% of magic tracks are not magic. Technically, they are sorcery.',
    "An ostrich's eye is bigger than its brain.",
    'In Greek myth, the craftsman Daedalus invented human flight so a group of minotaurs would stop teasiing him about it.',
    'Humans can survive underwater - but not for very long.',
    'Raseph, the Semitic god of war and plague, had a gazelle growing out of his forehead.',
    'The plural of Surgeon General is Surgeons General. The past tense of Surgeons General is Surgeonsed General.',
    'Polymerase I polypeptide A is a human gene.',
    'Rats cannot throw up.',
    'Iguanas can stay underwater for 28.7 minutes.',
    'Human tapeworms can grow up to 22.9 meters.',
    "The Schrodinger's cat paradox outlines a situation in which a cat in a box must be considered, for all intents and purposes, simultaneously alive and dead. Schrodinger created this paradox as a justification for killing cats.",
    'Every square inch of the human body has 32 million bacteria on it.',
    'The sun is 330,330 times larger than Earth.',
    'The average life expectancy of a rhinoceros in captivity is 15 years.',
    'Volcano-ologists are experts in the studies of volcanoes.',
    'Avocados have the highest fiber and calories of any fruit.',
    'Avocados have the highest fiber and calories of any fruit. They are found in Australia.',
    'The Moon orbits the Earth every 27.32 days.',
    'The billionth digit of pi is nine.',
    'If you have trouble with counting, use the following mnemonic device: One, comes before two, comes before sixty. Comes after twelve, comes before six-trillion, comes after five-hundred and four. This will make your earlier counting difficulties seem like no big deal.',
    'A gallon of water weights 8.34 pounds.',
    'Hot water freezes quicker than cold water.',
    'Honey does not spoil.',
    'The average adult body contains half a pound of salt.',
    'A nanosecond lasts one billionth of a second.',
    "According to Norse legend, thunder god Thor's chariot was pulled across the sky by two goats.",
    "China produces the world's second largest crop of soybeans.",
    'Tungsten hs the highest melting point of any metal, at 3,410 degrees celsius.',
    'Gently cleaning the tongue twice a day is the most effective way to fight bad breath.',
    'Roman toothpaste was made with human urine. Urine as an ingredient in toothpaste continued to be used up into the 18th century.',
    'The Tariff Act of 1789, established to protect domestic manufacture, was the second statute ever enacted by the United States government.'
    "The value of pi is the ratio of any circle's circumference to its diameter, in Euclidean space.",
    'The Mexican-American War ended in 1848 with the signing of the Treaty of Guadalupe Hidalgo.',
    'In 1879, Sandford Fleming first proposed the adoption of worldwide standardized time zones at the Royal Canadian Institute.',
    'Marie Curie invented the theory of radioactivity, the treatment of radioactivity, and dying of radioactivity.',
    'At the end of The Seagull by Anton Chekhov, Konstantin kills himself.',
    'Contrary to popular belief, the Eskimo does not have one hundred different words for snow. They do however, have two hundred and thirty-four words for fudge.',
    'In Victorian England, a commoner was not allowed to look directly at the Queen, due to a belief at the time that the poor had the ability to steal thoughts. Science now believes that less than 4% of poor people are able to do this.',
    'In 1862, Abraham Lincoln signed the Emancipation Proclamation, freeing the slaves. Like everything he did, Lincoln freed the slaves while sleepwalking, and later had no memory of the event.',
    'In 1948, at the request of a dying boy, baseball legend Babe Ruth ate seventy-five hot dogs, then died of hot dog poisoning.',
    'William Shakespeare did not exist. His plays were masterminded by Francis Bacon, who used a Ouija board to enslave play-writing ghosts.',
    'It is incorrectly noted that Thomas Edison invented push-ups in 1878. Nikolai Tesla had in fact patented the activity three years earlier, uner the name Tesla-cize.',
    'Whales are twice as intelligent and three times as delicioius as humans.',
    'The automobile brake was not invented until 1895. Before this, someone had to remain in the car at all times, driving circles until passengers returned from their errands.',
    'Edmund Hillary, the first person to climb Mount Everest, did so accidentally, while chasing a bird.',
    'Diamonds are made when coal is put under intense pressure become foam pellets, commonly used today as packing material.',
    "The most poisonous fish in the world is the orange ruffy. Everything but its eyes are made of a deadly poison. The ruffy's eyes are composed of a less harmful deadly poison.",
    "The occupation of court jester was invented accidentally, when a vassal's epilepsy was mistaken for capering.",
    "Haley's Comet can be viewed orbiting Earth every seventy-six years. For the other seventy-five, it retreats to the heart of the sun where it hibernates undisturbed.",
    'The first commercial airline flight took to the air in 1914. Everyone involved screamed the entire way.',
    'In Greek myth, Prometheus stole fire from the Gods and gave it to humankind. The jewelry he kept for himself.',
    "The first person to prove that cow's milk is drinkable was very, very thirsty.",
    'Before the Wright Brothers invented the airplane, anyone wanting to fly anywhere was required to eat 200 pounds of helium.',
    'Before the invention of scrambled eggs in 1912, the typical breakfast was either whole eggs still in the shell or scrambled rocks.',
    'During the Great Depression, the Tennessee Valley Authority outlawed pet rabbits, forcing many to hot glue-gun long ears onto their pet mice.',
    'At some point in their lives, 1 in 6 children will be abducted by the Dutch.',
    "According to most advanced algorithms, the world's best name is Craig.",
    'To make a photocopier, simple photocopy a mirror.',
    "Dreams are the subconscious mind's way of reminding people to go to school naked, and have their teeth fall out."
    ]

parser = ArgumentParser()
parser.add_argument('--channels', nargs='+', help='the channels factsphere will join')
parser.add_argument('--host', required=True, help='the host to connect to')
parser.add_argument('--port', default=6667, type=int, help='the port to use')
parser.add_argument('--nick', default='factsphere', help="factsphere's nick")

args = parser.parse_args()

irc = irclib.IRC()
server = irc.server()
server.connect(args.host, args.port, args.nick)
def _read_message(connection, event):
    if event.arguments()[0].rstrip() != '!fact': return
    # if a public message, we need to check the channel in target
    # if a private message, we need to check the person in source
    if event.eventtype() == 'pubmsg': target = event.target()
    else: target = event.source()
    # get message to send
    msg = quotes[random.randrange(0, len(quotes))]
    connection.privmsg(target, msg)
server.add_global_handler('pubmsg', _read_message)
server.add_global_handler('privmsg', _read_message)
if args.channels:
    for x in args.channels:
        server.join(x)
else:
    print 'warning: factsphere has not been told to enter any channels'

try:
    irc.process_forever()
except KeyboardInterrupt:
    server.quit('Corruption at 100%')
