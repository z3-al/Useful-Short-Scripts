for region in `aws ec2 describe-regions --region us-east-1 --output text | cut -f4`
do
     echo -e "\nListing Instances in region:'$region'..."
     aws ec2 describe-instances --region $region
done
