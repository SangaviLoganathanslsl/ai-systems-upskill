"""
This is a basic agent structure that will be built on a daily basis - with key functionalities added incrementally
1. creating an agent class with just a run method and default requirements

"""

class Agent():
    """
    """


    def __init__(self, name, description,task_list = None):
        self.name = name
        self.description = description
        self.task_list = []

    def __str__(self):
        string_to_print = f"I am agent {self.name},My job is to {self.description}!"
        return string_to_print
        
    def __repr__(self,action_str):
        return f"{action_str}"

    def run(self, task, action_str):
        """
        Print out the name of the agent and the task it is supposed to do
        """

        #append task to task_list
        self.task_list.append(task)

        # call repr
        repr(action_str)



        # returns the result of the dunder method __self__
        return str(self)


# initialise agents
# greeter
greeter = Agent("Greeter","Provide a pleasant greeting")

#lazygreeter
lazy = Agent("lazyGreeter","Provide a sloppy greeting")


# print agent instances
print(greeter)
print(lazy)

# give new tasks to the agents
greeter.run(task = "afternoon_greet",action_str = "Hello Goodafternoon")
lazy.run(task = "lazy_afternoongreet",action_str = "Ugh! its afternoon, Im sleepy, Good Afternoon anyways!")

# print the task list of each agent
print(greeter.task_list)
print(lazy.task_list)

# add more tasks to the agents
greeter.run(task = "evening_greet", action_str = "Hello Good Evening!")
lazy.run(task = "lazy_evening_greet", action_str = "Evenings make me lazy with not much brightness, not a good evening!")

# print the task list of each agent 
print(greeter.task_list)
print(lazy.task_list)

