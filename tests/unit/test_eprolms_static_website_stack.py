import aws_cdk as core
import aws_cdk.assertions as assertions

from eprolms_static_website.eprolms_static_website_stack import EprolmsStaticWebsiteStack

# example tests. To run these tests, uncomment this file along with the example
# resource in eprolms_static_website/eprolms_static_website_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = EprolmsStaticWebsiteStack(app, "eprolms-static-website")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
