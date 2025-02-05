import google.generativeai as genai
from django.shortcuts import render
from .models import Restaurant, TargetAudience

# Configure Gemini API
genai.configure(api_key="AIzaSyAxEnxrKBiSZV7zuoH64_ScBD5NJWGGTls")  # Replace with actual API key

# Dummy data for one restaurant and one target audience (Replace with actual data from your DB)
restaurant = Restaurant.objects.get(id=4)
target_audience = TargetAudience.objects.get(id=4)


def generate_content(request):
    # Prepare the prompt for Twitter content
    twitter_prompt = f"""
    Restaurant Information:
    Name: {restaurant.name}
    Tagline: {restaurant.tagline}
    Cuisine: {restaurant.cuisine}
    Location: {restaurant.location}
    Atmosphere: {restaurant.atmosphere}
    Hours of Operation: {restaurant.hours_of_operation}
    Delivery Options: {restaurant.delivery_options}

    Target Audience:
    Age Group: {target_audience.age_group}
    Income Level: {target_audience.income_level}
    Preferences: {target_audience.preferences}
    Engagement Platforms: {target_audience.engagement_platforms}

    Please generate viral content for Twitter based on the above restaurant and target audience information:
    1. Twitter Post
    """

    # Prepare the prompt for LinkedIn content
    linkedin_prompt = f"""
    Restaurant Information:
    Name: {restaurant.name}
    Tagline: {restaurant.tagline}
    Cuisine: {restaurant.cuisine}
    Location: {restaurant.location}
    Atmosphere: {restaurant.atmosphere}
    Hours of Operation: {restaurant.hours_of_operation}
    Delivery Options: {restaurant.delivery_options}

    Target Audience:
    Age Group: {target_audience.age_group}
    Income Level: {target_audience.income_level}
    Preferences: {target_audience.preferences}
    Engagement Platforms: {target_audience.engagement_platforms}

    Please generate viral content for LinkedIn based on the above restaurant and target audience information:
    1. LinkedIn Post
    """

    # Prepare the prompt for Instagram content
    instagram_prompt = f"""
    Restaurant Information:
    Name: {restaurant.name}
    Tagline: {restaurant.tagline}
    Cuisine: {restaurant.cuisine}
    Location: {restaurant.location}
    Atmosphere: {restaurant.atmosphere}
    Hours of Operation: {restaurant.hours_of_operation}
    Delivery Options: {restaurant.delivery_options}

    Target Audience:
    Age Group: {target_audience.age_group}
    Income Level: {target_audience.income_level}
    Preferences: {target_audience.preferences}
    Engagement Platforms: {target_audience.engagement_platforms}

    Please generate viral content for Instagram based on the above restaurant and target audience information:
    1. Instagram Post
    """

    # Call Gemini API for Twitter content
    twitter_model = genai.GenerativeModel("gemini-1.5-flash")
    twitter_response = twitter_model.generate_content(twitter_prompt)
    twitter_content = twitter_response.text

    # Call Gemini API for LinkedIn content
    linkedin_model = genai.GenerativeModel("gemini-1.5-flash")
    linkedin_response = linkedin_model.generate_content(linkedin_prompt)
    linkedin_content = linkedin_response.text

    # Call Gemini API for Instagram content
    instagram_model = genai.GenerativeModel("gemini-1.5-flash")
    instagram_response = instagram_model.generate_content(instagram_prompt)
    instagram_content = instagram_response.text

    # Add analysis prompts for each platform
    twitter_analysis_prompt = """
    Based on the restaurant and target audience information, provide strategic analysis for Twitter marketing:
    1. Best posting times
    2. Optimal hashtag strategy
    3. Content type that performs best
    4. Engagement tactics
    5. Common mistakes to avoid
    """
    
    linkedin_analysis_prompt = """
    Based on the restaurant and target audience information, provide strategic analysis for LinkedIn marketing:
    1. Professional tone guidelines
    2. Content themes that resonate
    3. Best practices for business engagement
    4. Networking opportunities
    5. Performance metrics to track
    """
    
    # Instagram analysis prompt with detailed growth strategy
    instagram_analysis_prompt = f"""
    Based on {restaurant.name} ({restaurant.cuisine} cuisine) and target audience ({target_audience.age_group}, {target_audience.income_level}), 
    provide a comprehensive Instagram growth strategy:

    1. Content Strategy:
       - Best content types for this restaurant
       - Optimal posting schedule
       - Story/Reel ideas specific to the cuisine
       - Photography tips for {restaurant.cuisine} dishes

    2. Audience Growth:
       - Engagement tactics for {target_audience.age_group}
       - Local hashtag strategy for {restaurant.location}
       - Collaboration opportunities
       - Contest and giveaway ideas

    3. Brand Building:
       - Visual identity tips
       - Bio optimization
       - Highlight categories
       - Location tagging strategy

    4. Monetization:
       - Promotion strategies
       - Booking/reservation features
       - Menu highlighting tactics
       - Special offers presentation

    5. Analytics Focus:
       - Key metrics to track
       - Best times to post
       - Competitor analysis tips
       - Content performance tracking
    """
    
    # Generate analysis content
    twitter_analysis = twitter_model.generate_content(twitter_analysis_prompt).text
    linkedin_analysis = linkedin_model.generate_content(linkedin_analysis_prompt).text
    instagram_analysis = instagram_model.generate_content(instagram_analysis_prompt).text
    
    # Prepare context to render in template
    context = {
        'restaurant': restaurant,
        'target_audience': target_audience,
        'twitter_post': twitter_content,
        'linkedin_post': linkedin_content,
        'instagram_post': instagram_content,
        'twitter_analysis': twitter_analysis,
        'linkedin_analysis': linkedin_analysis,
        'instagram_analysis': instagram_analysis,
    }

    return render(request, 'generate_content.html', context)


