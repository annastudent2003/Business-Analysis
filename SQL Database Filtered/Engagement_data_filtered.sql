SELECT 
    EngagementID, 
    ContentID, 
    CampaignID, 
    ProductID, 
    UPPER(REPLACE(ContentType, 'Socialmedia', 'Social Media')) AS ContentType,
    
    SUBSTRING_INDEX(ViewsClicksCombined, '-', 1) AS Views,
    SUBSTRING_INDEX(ViewsClicksCombined, '-', -1) AS Clicks,
    
    Likes,
    DATE_FORMAT(EngagementDate, '%d.%m.%Y') AS EngagementDate
FROM business.`dbo.engagement_data`
WHERE ContentType != 'Newsletter';
