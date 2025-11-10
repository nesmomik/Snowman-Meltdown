# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

# Number of snowman stages
MAX_MISTAKES = 4

# Snowman ASCII Art stages
STAGES = [
    # Stage 0: Full snowman
    """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     ( : ) 
     """,
    # Stage 1: Bottom part starts melting
    """

      ___  
     /___\\ 
     (o o) 
     ( : ) 
     """,
    # Stage 2: Only the head remains
    """


      ___  
     /___\\ 
     (o o) 
     """,
    # Stage 3: Snowman completely melted
    """



      ___  
     /___\\ 
     """,
    """




      ___  
     """,
]
