class Profile:
    #initialize the variables
    profile = 0
   
    #define the constructor
    def __init__(self, variesProfile):
        self.profile = variesProfile

    #define class methods
    def define_profile(self):
        collection_profile = {
            'profile' : [
                (f'/html/body/div[2]/div/div/div[2]/ul/div/li[{self.profile}]/div/div[1]/div[2]/div[1]/a'), 
                (f'/html/body/div[3]/div/div/div[2]/ul/div/li[{self.profile}]/div/div[1]/div[2]/div[1]/a'),
                (f'/html/body/div[1]/div/div/div[2]/ul[1]/div/li[{self.profile}]/div/div[1]/div/a'),
                (f'/html/body/div[2]/div/div/div[2]/ul[1]/div/li[{self.profile}]/div/div[1]/div/a'),
                (f'/html/body/div[3]/div/div/div[2]/ul[1]/div/li[{self.profile}]/div/div[1]/div/a'),

                (f'/html/body/div[1]/div/div/div[2]/ul[1]/div/li[{self.profile}]/div/div[2]/div[1]/div/div/a'),
                (f'/html/body/div[2]/div/div/div[2]/ul[1]/div/li[{self.profile}]/div/div[2]/div[1]/div/div/a'),
                (f'/html/body/div[3]/div/div/div[2]/ul[1]/div/li[{self.profile}]/div/div[2]/div[1]/div/div/a'),
                (f'/html/body/div[1]/div/div/div[2]/ul/div/li[{self.profile}]/div/div[2]/div[1]/div/div/a'),
                (f'/html/body/div[1]/div/div/div[2]/ul/div/li[{self.profile}]/div/div[1]/div[2]/div[1]/a'),

                (f'/html/body/div[2]/div/div/div[2]/ul/div/li[{self.profile}]/div/div[2]/div[1]/div/div/a'),
                (f'/html/body/div[2]/div/div[2]/ul/div/li[{self.profile}]/div/div[2]/div[1]/div/div/a'),
                (f'/html/body/div[2]/div/div[2]/ul/div/li[{self.profile}]/div/div[1]/div[2]/div[1]/a'),
                (f'/html/body/div[1]/div/div[2]/ul/div/li[{self.profile}]/div/div[2]/div[1]/div/div/a'),
                (f'/html/body/div[1]/div/div[2]/ul/div/li[{self.profile}]/div/div[1]/div[2]/div[1]/a'),

                f'/html/body/div[2]/div/div[2]/ul/div/li[{self.profile}]/div/div[1]/div[2]/div[1]/a',
                f'/html/body/div[1]/div/div[2]/ul/div/li[{self.profile}]/div/div[1]/div[2]/div[1]/a',
                f'/html/body/div[3]/div/div[2]/ul/div/li[{self.profile}]/div/div[1]/div[2]/div[1]/a'
            ]
        }
        return collection_profile 

class Interact:
    #initialize the variables
    element = 0
    number = 0

    #define the constructor
    def __init__(self, variesElement, variesNumber):
        self.element = variesElement
        self.number = variesNumber 

    #define class methods
    def define_interact(self):
        collection_interact = {
            'interact' : [
                (f"//*[@id='react-root']/section/main/div/div[4]/article/div[1]/div/div[{self.element}]/div[{self.number}]"),
                (f"//*[@id='react-root']/section/main/div/div[3]/article/div[1]/div/div[{self.element}]/div[{self.number}]"),
                (f"//*[@id='react-root']/section/main/div/div[2]/article/div[1]/div/div[{self.element}]/div[{self.number}]"),
                (f"//*[@id='react-root']/section/main/div/div[1]/article/div[1]/div/div[{self.element}]/div[{self.number}]"),

                f'//*[@id="react-root"]/section/main/div/div[3]/article/div[{self.element}]/div/div[{self.number}]',
                f'//*[@id="react-root"]/section/main/div/div[2]/article/div[{self.element}]/div/div[{self.number}]',
                f'//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div[{self.element}]/div[{self.number}]',
                f'//*[@id="react-root"]/section/main/div/div[2]/article/div[1]/div/div[{self.element}]/div[{self.number}]'
            ]
        }
        return collection_interact

    
alternate = {
    'pulse' : [
        '/html/body/div[3]/div[2]/div/article/div[2]/section[1]/span[1]/button',
        '/html/body/div[2]/div[2]/div/article/div[2]/section[1]/span[1]/button'
    ],
    'following' : [
        '//*[@id="react-root"]/section/main/div/header/section/div[1]/button',
        '//*[@id="react-root"]/section/main/div/header/section/div[1]/span/span[1]/button',
        '//*[@id="react-root"]/section/main/div/header/section/div[1]/span[2]/span[1]/button',
        '//*[@id="react-root"]/section/main/div/header/section/div[2]/span/span[1]/button'
    ],
    'unfollowing' : [
        '/html/body/div[3]/div/div/div/div[3]/button[1]',
        '/html/body/div[2]/div/div/div/div[3]/button[1]',

        '/html/body/div[3]/div/div/div[3]/button[1]',
        '/html/body/div[2]/div/div/div[3]/button[1]'
    ],
    'internal_gates' : [
        '//*[@id="react-root"]/section/main/div/header/section/ul/li[1]/span/span'
    ],
    'degree_n1' : [
        '//*[@id="react-root"]/section/main/div/div/article/div/div/h2',
        '//*[@id="react-root"]/section/main/div/div[2]/article/div/div/h2',
        '//*[@id="react-root"]/section/main/div/div/article/div[1]/div/h2',
        '//*[@id="react-root"]/section/main/div/div[2]/article/div[1]/div/h2',
        
        
        '//*[@id="react-root"]/section/main/div/div/article/div[1]/div/h2',
        
        '//*[@id="react-root"]/section/main/div/div[3]/article/div/div/div[2]/h1',
        '//*[@id="react-root"]/section/main/div/div[2]/article/div/div/div[2]/h1',
        
        '/html/body/div/div[1]/div/div/h2',
    ],
    'degree_n4' : [
        '//*[@id="react-root"]/section/main/div/header/section/div[2]/span',
        '//*[@id="react-root"]/section/main/div/header/section/div[1]/h1'
    ],
    'comment' : {
        'prime' : [
            '/html/body/div[2]/div[2]/div/article/div[2]/section[1]/span[2]/button'
        ],
        'path' : [
            '/html/body/div[2]/div[2]/div/article/div[2]/section[3]/div/form/textarea',
            
            '/html/body/div[3]/div/div[2]/div/article/div[2]/section[3]/div/form/textarea',
            '/html/body/div[2]/div/div[2]/div/article/div[2]/section[3]/div/form/textarea'

        ],
        'exchange' : [
            "Love!",
            "J'adore",
            "Love this!",
            "J'adore!",
            "Love This! <3",
            "J'aime!",
            "#Love",
            "J'aime <3", 
            "Love :-)",
            "Love <3",
            "<3"
        ]
        
    },
    'retract' : {
        'notification' : [
            '/html/body/div[2]/div/div/div[3]/button[2]',
            '/html/body/div[3]/div/div/div[3]/button[2]'
        ],
        'user_entry' : [
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]/a'
        ],
        'user_list' : [
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a'
        ]
    },
    'prime_authenticate' : [
        '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/button',
        '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button',
        '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[5]/button'
    ]
}


alternate_ratio = {
    'post' : [
        '//*[@id="react-root"]/section/main/div/header/section/ul/li[1]/span/span',
        '//*[@id="react-root"]/section/main/div/ul/li[1]/span/span'
    ],
    'followers' : [
        '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span',
        '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/span/span',
        '//*[@id="react-root"]/section/main/div/ul/li[2]/a/span'
    ],
    'following' : [
        '//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span',
        '//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/span/span',
        '//*[@id="react-root"]/section/main/div/ul/li[3]/a/span'
    ]
}



