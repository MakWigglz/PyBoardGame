import sqlite3

def setup_database():
    conn = sqlite3.connect('board_game.db')
    cursor = conn.cursor()

    # Create table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS content (
            id INTEGER PRIMARY KEY,
            row INTEGER,
            col INTEGER,
            paragraph TEXT
        )
    ''')

    # Insert sample data for 64 squares (8x8 board)
    topics = [f"Topic {i+1}" for i in range(64)]
    for row in range(8):
        for col in range(8):
            topic_index = row * 8 + col
            topic = topics[topic_index]
            
            if topic_index == 0:
                paragraphs = [
                    "Ecology is a branch of biology that examines the interactions between organisms and their environment. Ecologists study the relationships among living organisms, including humans, and their physical surroundings, as well as the processes that influence the distribution and abundance of species. This field is vital for understanding the dynamics of ecosystems, the impact of human activities on natural habitats, and the importance of biodiversity. Ecological research informs conservation efforts, guiding policies to protect endangered species and manage natural resources sustainably.",
                    "Finally, physiology explores the functions and mechanisms of living systems. It investigates how organisms perform vital functions, such as respiration, circulation, and digestion, and how these processes are regulated and coordinated. Physiology also examines how organisms respond to external stimuli and maintain homeostasis—a stable internal environment. Advances in physiology have profound implications for medicine and health, as they provide insights into disease mechanisms and inform the development of treatments and interventions to improve human well-being.",
                    "Biology is a dynamic and ever-evolving field that continues to expand our understanding of the natural world and our place within it. By studying the complexities of life, biologists contribute to advancements in medicine, agriculture, environmental protection, and many other areas that impact our daily lives. By examining the basic building blocks of life—cells and genes—biologists strive to uncover the fundamental processes that drive the development and functioning of organisms.",
                    "One of the central themes in biology is the concept of evolution, which explains the diversity of life on Earth. The theory of evolution, first articulated by Charles Darwin, posits that all species of organisms arise and develop through natural selection, which favors the survival and reproduction of individuals with advantageous traits. This process of descent with modification has led to the vast array of species that inhabit our planet, each uniquely adapted to its environment. Understanding evolutionary principles helps biologists trace the lineage of organisms and predict how species might adapt to changing conditions.",
                    "Another crucial area of biology is genetics, the study of heredity and variation in organisms. Genetics delves into how traits are passed from one generation to the next through the inheritance of genes, the basic units of heredity. The field has advanced significantly with the advent of molecular biology techniques, allowing scientists to manipulate and analyze DNA, the molecule that carries genetic information. These breakthroughs have paved the way for developments in biotechnology, such as genetic engineering and gene therapy, which hold promise for treating genetic disorders and improving crop yields."
                ]
            elif topic_index == 1:
                paragraphs = [
                    "Astronomy also delves into the enigmatic realms of black holes and dark matter. Black holes are regions of spacetime where gravity is so intense that not even light can escape. They are formed from the remnants of massive stars and are often found at the centers of galaxies, including our own Milky Way. Dark matter, on the other hand, is a mysterious substance that does not emit, absorb, or reflect light, yet it exerts gravitational forces on visible matter. Together with dark energy, dark matter makes up about 95 percent of the universe's total mass-energy content. Understanding these elusive components is crucial for unraveling the fundamental nature of the cosmos.",
                    "Finally, cosmology, a branch of astronomy, focuses on the study of the universe as a whole, including its origin, structure, evolution, and eventual fate. The Big Bang theory, which posits that the universe began as an extremely hot and dense point about 13.8 billion years ago, is the prevailing cosmological model. Observations of the cosmic microwave background radiation, the large-scale structure of the universe, and the accelerating expansion of the cosmos provide evidence supporting this theory. Cosmologists also explore the potential existence of parallel universes, the nature of time, and the ultimate fate of the universe, seeking answers to some of the most profound questions about existence.",
                    "Astronomy continues to push the boundaries of human knowledge, revealing the wonders of the universe and our place within it. Through advanced telescopes, space missions, and theoretical research, astronomers strive to unlock the secrets of the cosmos, expanding our understanding of the vast and mysterious universe that surrounds us. One of the central areas of study in astronomy is the observation and analysis of stars. Stars are luminous celestial bodies composed primarily of hydrogen and helium, undergoing nuclear fusion reactions in their cores. Astronomers study stars to understand their life cycles, from formation in stellar nurseries to their eventual demise as white dwarfs, neutron stars, or black holes. By examining the light emitted by stars, astronomers can determine their composition, temperature, distance, and motion, providing insights into the dynamics of galaxies and the evolution of the universe.",
                    "Planets and their moons also captivate astronomers, particularly those within our solar system. Each planet offers a unique glimpse into the diverse processes shaping celestial bodies. For example, the study of Mars has revealed evidence of ancient riverbeds and the potential for past microbial life. Meanwhile, the exploration of the icy moons of Jupiter and Saturn has uncovered subsurface oceans that could harbor life. Understanding the geology, atmospheres, and potential habitability of these celestial neighbors helps astronomers develop theories about the formation of planetary systems and the potential for life beyond Earth.",
                    "One of the central areas of study in astronomy is the observation and analysis of stars. Stars are luminous celestial bodies composed primarily of hydrogen and helium, undergoing nuclear fusion reactions in their cores. Astronomers study stars to understand their life cycles, from formation in stellar nurseries to their eventual demise as white dwarfs, neutron stars, or black holes. By examining the light emitted by stars, astronomers can determine their composition, temperature, distance, and motion, providing insights into the dynamics of galaxies and the evolution of the universe.",
                    "Planets and their moons also captivate astronomers, particularly those within our solar system. Each planet offers a unique glimpse into the diverse processes shaping celestial bodies. For example, the study of Mars has revealed evidence of ancient riverbeds and the potential for past microbial life. Meanwhile, the exploration of the icy moons of Jupiter and Saturn has uncovered subsurface oceans that could harbor life. Understanding the geology, atmospheres, and potential habitability of these celestial neighbors helps astronomers develop theories about the formation of planetary systems and the potential for life beyond Earth."
                ]
            elif topic_index == 2:
                paragraphs = [
					"Neuroscience is the study of the nervous system, including the brain and spinal cord.",
					"Neuroscience encompasses a wide range of topics, from the structure and function of neurons to the complex interactions between different brain regions. Neuroscientists investigate how the brain processes information, controls behavior, and gives rise to consciousness. They explore the neural mechanisms underlying learning, memory, perception, and decision-making. By studying the brain's wiring diagram, neuroscientists seek to understand how it enables us to perceive, think, feel, and interact with the world around us.",
					"Neuroscience is a rapidly evolving field, with new discoveries and insights emerging regularly. Advances in technology, such as advanced imaging techniques and genetic manipulation, have revolutionized the way neuroscientists study the brain. These advancements have allowed researchers to visualize the brain's structure and function in unprecedented detail, enabling them to explore the intricate connections between neurons and the neural networks that govern our behavior and cognition.",
					"Neuroscience has applications in various fields, including medicine, psychology, and artificial intelligence. Understanding the brain's mechanisms can lead to the development of new treatments for neurological disorders, such as Alzheimer's disease and Parkinson's disease. Additionally, neuroscience contributes to our understanding of human behavior and cognition, shedding light on the complex interplay between genetics, environment, and experience. By unraveling the mysteries of the brain, neuroscience continues to expand our knowledge of the human mind and pave the way for groundbreaking discoveries in the future.",
					"Advances in technology, such as advanced imaging techniques and genetic manipulation, have revolutionized the way neuroscientists study the brain. These advancements have allowed researchers to visualize the brain's structure and function in unprecedented detail"
				]
            elif topic_index == 3:
                paragraphs = [
                    "The study of the human body is a vast and fascinating field that encompasses various disciplines and specialties. From the microscopic world of cells to the macroscopic realm of organs and systems, the human body offers endless opportunities for exploration and discovery. In this article, we will delve into the fascinating world of the human body, exploring its structure, functions, and the intricate mechanisms that govern our existence.",
					"The human body is a marvel of engineering, composed of trillions of cells that work together to maintain homeostasis and enable us to perform daily activities. Each cell is a complex entity, containing specialized organelles that carry out specific functions. The human body is divided into several systems, including the respiratory, circulatory, digestive, and nervous systems, among others. These systems work in harmony to ensure the proper functioning of the body.",
					"The human body is a marvel of engineering, composed of trillions of cells that work together to maintain homeostasis and enable us to perform daily activities. Each cell is a complex entity, containing specialized organelles that carry out specific functions. The human body is divided into several systems, including the respiratory, circulatory, digestive, and nervous systems, among others. These systems work in harmony to ensure the proper functioning of the body.",
					"The human body is a marvel of engineering, composed of trillions of cells that work together to maintain homeostasis and enable us to perform daily activities. Each cell is a complex entity, containing specialized organelles that carry out specific functions. The human body is divided into several systems, including the respiratory, circulatory, digestive, and nervous systems, among others. These systems work in harmony to ensure the proper functioning of the body.",
					"The human body is a marvel of engineering, composed of trillions of cells that work together to maintain homeostasis and enable us to perform daily activities. Each cell is a complex entity, containing specialized organelles that carry out specific functions. The human body is divided into several systems, including the respiratory, circulatory, digestive, and nervous systems, among others. These systems work in harmony to ensure the proper functioning of the body."
				]	
            else:
                paragraphs = [
                    f"Paragraph 1 for {topic}",
                    f"Paragraph 2 for {topic}",
                    f"Paragraph 3 for {topic}",
                    f"Paragraph 4 for {topic}",
                    f"Paragraph 5 for {topic}"
                ]
            
            for paragraph in paragraphs:
                cursor.execute('''
                    INSERT INTO content (row, col, paragraph)
                    VALUES (?, ?, ?)
                ''', (row, col, paragraph))

    conn.commit()
    conn.close()

setup_database()