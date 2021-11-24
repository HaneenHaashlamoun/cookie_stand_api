# api-quick-start

https://github.com/HaneenHaashlamoun/cookie_stand_api/pulls/1

# Feature Tasks and Requirements
## Use API Quick Start Template
- [x] Create a new repo cookie-stand-api that uses API Quick Start as a template.
- [x] Modify your application using instructions in README.md found in root of repo.
  - [x] Change things app folder to be cookie_stands
  - [x] Go through code base looking for Thing,thing and things change to cookie-stand related names.
  - [x] E.g. Thing model becomes CookieStand
  - [x] E.g. ThingList becomes CookieStandList
- [x] Pro Tip: Do a global text search looking for thing
  - [x] Search should be case insensitive.

## Deeper CookieStand Changes
- [x] The CookieStand model must contain
```
 location = models.CharField(max_length=256)
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )
    description = models.TextField(default="", null=True, blank=True)
    hourly_sales = models.JSONField(default=list, blank=True)
    minimum_customers_per_hour = models.IntegerField(default=0)
    maximum_customers_per_hour = models.IntegerField(default=0)
    average_cookies_per_sale = models.FloatField(default=0)
```

## Database Deployment Requirements
- [x] Host your Database at ElephantSQL

## Site Deployment Requirements
- [x] Deploy Docker container to Heroku
