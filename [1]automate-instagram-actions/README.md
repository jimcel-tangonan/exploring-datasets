### Explanation of interesting bits of code

At the Login Page, your Instagram email and associated password will be inputed into the correct fields and submitted. 
![Alt text](_images/initialize.png?raw=true "initialize browser")


Two scripts, one dedicated to follow and another to unfollow, are preferentially initialized.
![Alt text](_images/evaluate.png?raw=true "evaluate user-login/password")


Since XPath varies between IG profile, multiple paths are taken into consideration for every click. 
- An xpath is used to navigate through elements and attributes in an XML document.
Parmeters are calculated at `internal_gates` and `external_gates`, and only when passed will the script continue. Otherwise, it will exit the IG-profile and onto the next profile evaluation. 
![Alt text](_images/engine_.png?raw=true "main logic")

To calculate the followers/following ratio, the value is preprocessed into an integer.
![Alt text](_images/ratio.png?raw=true "calculate followers/following ratio")


I've noticed that when a photo is liked, its class change into `'glyphsSpriteHeart__filled__24__red_5'`. If found, the function `cascade` becomes True and continues the script-actions, otherwise exiting the photo to choose another. Commenting is closely monitored and therefore is only initiated when the profile is divisible by 3.
- IG profile 1 : no comment
- IG profile 2 : no comment
- IG profile 3 : comment
- IG profile 4 : no comment
![Alt text](_images/pulse-comment.png?raw=true "liking and commenting")






