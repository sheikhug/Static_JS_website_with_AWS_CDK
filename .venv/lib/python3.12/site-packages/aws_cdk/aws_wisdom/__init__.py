r'''
# AWS::Wisdom Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_wisdom as wisdom
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Wisdom construct libraries](https://constructs.dev/search?q=wisdom)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Wisdom resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Wisdom.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Wisdom](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Wisdom.html).

(Read the [CDK Contributing Guide](https://github.com/aws/aws-cdk/blob/main/CONTRIBUTING.md) and submit an RFC if you are interested in contributing to this construct library.)

<!--END CFNONLY DISCLAIMER-->
'''
from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)

import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

import typeguard
from importlib.metadata import version as _metadata_package_version
TYPEGUARD_MAJOR_VERSION = int(_metadata_package_version('typeguard').split('.')[0])

def check_type(argname: str, value: object, expected_type: typing.Any) -> typing.Any:
    if TYPEGUARD_MAJOR_VERSION <= 2:
        return typeguard.check_type(argname=argname, value=value, expected_type=expected_type) # type:ignore
    else:
        if isinstance(value, jsii._reference_map.InterfaceDynamicProxy): # pyright: ignore [reportAttributeAccessIssue]
           pass
        else:
            if TYPEGUARD_MAJOR_VERSION == 3:
                typeguard.config.collection_check_strategy = typeguard.CollectionCheckStrategy.ALL_ITEMS # type:ignore
                typeguard.check_type(value=value, expected_type=expected_type) # type:ignore
            else:
                typeguard.check_type(value=value, expected_type=expected_type, collection_check_strategy=typeguard.CollectionCheckStrategy.ALL_ITEMS) # type:ignore

from .._jsii import *

import constructs as _constructs_77d1e7e8
from .. import (
    CfnResource as _CfnResource_9df397a6,
    CfnTag as _CfnTag_f6864754,
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    ITaggable as _ITaggable_36806126,
    ITaggableV2 as _ITaggableV2_4e6798f8,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnAIAgent(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_wisdom.CfnAIAgent",
):
    '''Creates an Amazon Q in Connect AI Agent.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiagent.html
    :cloudformationResource: AWS::Wisdom::AIAgent
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_wisdom as wisdom
        
        cfn_aIAgent = wisdom.CfnAIAgent(self, "MyCfnAIAgent",
            assistant_id="assistantId",
            configuration=wisdom.CfnAIAgent.AIAgentConfigurationProperty(
                answer_recommendation_ai_agent_configuration=wisdom.CfnAIAgent.AnswerRecommendationAIAgentConfigurationProperty(
                    answer_generation_ai_prompt_id="answerGenerationAiPromptId",
                    association_configurations=[wisdom.CfnAIAgent.AssociationConfigurationProperty(
                        association_configuration_data=wisdom.CfnAIAgent.AssociationConfigurationDataProperty(
                            knowledge_base_association_configuration_data=wisdom.CfnAIAgent.KnowledgeBaseAssociationConfigurationDataProperty(
                                content_tag_filter=wisdom.CfnAIAgent.TagFilterProperty(
                                    and_conditions=[wisdom.CfnAIAgent.TagConditionProperty(
                                        key="key",
        
                                        # the properties below are optional
                                        value="value"
                                    )],
                                    or_conditions=[wisdom.CfnAIAgent.OrConditionProperty(
                                        and_conditions=[wisdom.CfnAIAgent.TagConditionProperty(
                                            key="key",
        
                                            # the properties below are optional
                                            value="value"
                                        )],
                                        tag_condition=wisdom.CfnAIAgent.TagConditionProperty(
                                            key="key",
        
                                            # the properties below are optional
                                            value="value"
                                        )
                                    )],
                                    tag_condition=wisdom.CfnAIAgent.TagConditionProperty(
                                        key="key",
        
                                        # the properties below are optional
                                        value="value"
                                    )
                                ),
                                max_results=123,
                                override_knowledge_base_search_type="overrideKnowledgeBaseSearchType"
                            )
                        ),
                        association_id="associationId",
                        association_type="associationType"
                    )],
                    intent_labeling_generation_ai_prompt_id="intentLabelingGenerationAiPromptId",
                    query_reformulation_ai_prompt_id="queryReformulationAiPromptId"
                ),
                manual_search_ai_agent_configuration=wisdom.CfnAIAgent.ManualSearchAIAgentConfigurationProperty(
                    answer_generation_ai_prompt_id="answerGenerationAiPromptId",
                    association_configurations=[wisdom.CfnAIAgent.AssociationConfigurationProperty(
                        association_configuration_data=wisdom.CfnAIAgent.AssociationConfigurationDataProperty(
                            knowledge_base_association_configuration_data=wisdom.CfnAIAgent.KnowledgeBaseAssociationConfigurationDataProperty(
                                content_tag_filter=wisdom.CfnAIAgent.TagFilterProperty(
                                    and_conditions=[wisdom.CfnAIAgent.TagConditionProperty(
                                        key="key",
        
                                        # the properties below are optional
                                        value="value"
                                    )],
                                    or_conditions=[wisdom.CfnAIAgent.OrConditionProperty(
                                        and_conditions=[wisdom.CfnAIAgent.TagConditionProperty(
                                            key="key",
        
                                            # the properties below are optional
                                            value="value"
                                        )],
                                        tag_condition=wisdom.CfnAIAgent.TagConditionProperty(
                                            key="key",
        
                                            # the properties below are optional
                                            value="value"
                                        )
                                    )],
                                    tag_condition=wisdom.CfnAIAgent.TagConditionProperty(
                                        key="key",
        
                                        # the properties below are optional
                                        value="value"
                                    )
                                ),
                                max_results=123,
                                override_knowledge_base_search_type="overrideKnowledgeBaseSearchType"
                            )
                        ),
                        association_id="associationId",
                        association_type="associationType"
                    )]
                )
            ),
            type="type",
        
            # the properties below are optional
            description="description",
            name="name",
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        assistant_id: builtins.str,
        configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnAIAgent.AIAgentConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param assistant_id: The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
        :param configuration: Configuration for the AI Agent.
        :param type: The type of the AI Agent.
        :param description: The description of the AI Agent.
        :param name: The name of the AI Agent.
        :param tags: The tags used to organize, track, or control access for this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4d43de9ccaeb31eba5b0b613ecac25531a87bb9137652388e6196070f4622ab)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAIAgentProps(
            assistant_id=assistant_id,
            configuration=configuration,
            type=type,
            description=description,
            name=name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__daf9bd162ab4eaa6b11972bcaf8372498a47b4ad8cf111130cabfae3f675d2b4)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__569f9e85834b9b380045c7e9789b3ac0684022e3b37642b34e232ba9b451ade6)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAiAgentArn")
    def attr_ai_agent_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the AI agent.

        :cloudformationAttribute: AIAgentArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAiAgentArn"))

    @builtins.property
    @jsii.member(jsii_name="attrAiAgentId")
    def attr_ai_agent_id(self) -> builtins.str:
        '''The identifier of the AI Agent.

        :cloudformationAttribute: AIAgentId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAiAgentId"))

    @builtins.property
    @jsii.member(jsii_name="attrAssistantArn")
    def attr_assistant_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the Amazon Q in Connect assistant.

        :cloudformationAttribute: AssistantArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAssistantArn"))

    @builtins.property
    @jsii.member(jsii_name="cdkTagManager")
    def cdk_tag_manager(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "cdkTagManager"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="assistantId")
    def assistant_id(self) -> builtins.str:
        '''The identifier of the Amazon Q in Connect assistant.'''
        return typing.cast(builtins.str, jsii.get(self, "assistantId"))

    @assistant_id.setter
    def assistant_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3d8fd38839efd97edc463e08adcbeb6d1b964aa278b19d07017fb40c806bb19)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assistantId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="configuration")
    def configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnAIAgent.AIAgentConfigurationProperty"]:
        '''Configuration for the AI Agent.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnAIAgent.AIAgentConfigurationProperty"], jsii.get(self, "configuration"))

    @configuration.setter
    def configuration(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnAIAgent.AIAgentConfigurationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d07c289ddb2abe8b14c5f581386f3377fb7266b5b099c89c1b142b4bbd9d769)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configuration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''The type of the AI Agent.'''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b90fdd18e60e92e1589e2bf61b55c6cd7758b9da5e26d00525cb08a2ad13830)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the AI Agent.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6380f3badbada0c208691bd5242dfabe1122f10b446d77f1ae5ad0c9da456ae8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the AI Agent.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__982490f39ff188d23898421a1623ad1489db32be592625d58e01c368c7568247)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags used to organize, track, or control access for this resource.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e3ed01afbf4aa2c01303d467dcbf5c5cd3fb267902b917f3c4f5fdd0d83ccdc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnAIAgent.AIAgentConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "answer_recommendation_ai_agent_configuration": "answerRecommendationAiAgentConfiguration",
            "manual_search_ai_agent_configuration": "manualSearchAiAgentConfiguration",
        },
    )
    class AIAgentConfigurationProperty:
        def __init__(
            self,
            *,
            answer_recommendation_ai_agent_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAIAgent.AnswerRecommendationAIAgentConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            manual_search_ai_agent_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAIAgent.ManualSearchAIAgentConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''A typed union that specifies the configuration based on the type of AI Agent.

            :param answer_recommendation_ai_agent_configuration: The configuration for AI Agents of type ``ANSWER_RECOMMENDATION`` .
            :param manual_search_ai_agent_configuration: The configuration for AI Agents of type ``MANUAL_SEARCH`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-aiagentconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                a_iAgent_configuration_property = wisdom.CfnAIAgent.AIAgentConfigurationProperty(
                    answer_recommendation_ai_agent_configuration=wisdom.CfnAIAgent.AnswerRecommendationAIAgentConfigurationProperty(
                        answer_generation_ai_prompt_id="answerGenerationAiPromptId",
                        association_configurations=[wisdom.CfnAIAgent.AssociationConfigurationProperty(
                            association_configuration_data=wisdom.CfnAIAgent.AssociationConfigurationDataProperty(
                                knowledge_base_association_configuration_data=wisdom.CfnAIAgent.KnowledgeBaseAssociationConfigurationDataProperty(
                                    content_tag_filter=wisdom.CfnAIAgent.TagFilterProperty(
                                        and_conditions=[wisdom.CfnAIAgent.TagConditionProperty(
                                            key="key",
                
                                            # the properties below are optional
                                            value="value"
                                        )],
                                        or_conditions=[wisdom.CfnAIAgent.OrConditionProperty(
                                            and_conditions=[wisdom.CfnAIAgent.TagConditionProperty(
                                                key="key",
                
                                                # the properties below are optional
                                                value="value"
                                            )],
                                            tag_condition=wisdom.CfnAIAgent.TagConditionProperty(
                                                key="key",
                
                                                # the properties below are optional
                                                value="value"
                                            )
                                        )],
                                        tag_condition=wisdom.CfnAIAgent.TagConditionProperty(
                                            key="key",
                
                                            # the properties below are optional
                                            value="value"
                                        )
                                    ),
                                    max_results=123,
                                    override_knowledge_base_search_type="overrideKnowledgeBaseSearchType"
                                )
                            ),
                            association_id="associationId",
                            association_type="associationType"
                        )],
                        intent_labeling_generation_ai_prompt_id="intentLabelingGenerationAiPromptId",
                        query_reformulation_ai_prompt_id="queryReformulationAiPromptId"
                    ),
                    manual_search_ai_agent_configuration=wisdom.CfnAIAgent.ManualSearchAIAgentConfigurationProperty(
                        answer_generation_ai_prompt_id="answerGenerationAiPromptId",
                        association_configurations=[wisdom.CfnAIAgent.AssociationConfigurationProperty(
                            association_configuration_data=wisdom.CfnAIAgent.AssociationConfigurationDataProperty(
                                knowledge_base_association_configuration_data=wisdom.CfnAIAgent.KnowledgeBaseAssociationConfigurationDataProperty(
                                    content_tag_filter=wisdom.CfnAIAgent.TagFilterProperty(
                                        and_conditions=[wisdom.CfnAIAgent.TagConditionProperty(
                                            key="key",
                
                                            # the properties below are optional
                                            value="value"
                                        )],
                                        or_conditions=[wisdom.CfnAIAgent.OrConditionProperty(
                                            and_conditions=[wisdom.CfnAIAgent.TagConditionProperty(
                                                key="key",
                
                                                # the properties below are optional
                                                value="value"
                                            )],
                                            tag_condition=wisdom.CfnAIAgent.TagConditionProperty(
                                                key="key",
                
                                                # the properties below are optional
                                                value="value"
                                            )
                                        )],
                                        tag_condition=wisdom.CfnAIAgent.TagConditionProperty(
                                            key="key",
                
                                            # the properties below are optional
                                            value="value"
                                        )
                                    ),
                                    max_results=123,
                                    override_knowledge_base_search_type="overrideKnowledgeBaseSearchType"
                                )
                            ),
                            association_id="associationId",
                            association_type="associationType"
                        )]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8cb84ad0dc27ffdae65e4e739c98ea6a4e7c36340f15c21ae83a2225ff763ba3)
                check_type(argname="argument answer_recommendation_ai_agent_configuration", value=answer_recommendation_ai_agent_configuration, expected_type=type_hints["answer_recommendation_ai_agent_configuration"])
                check_type(argname="argument manual_search_ai_agent_configuration", value=manual_search_ai_agent_configuration, expected_type=type_hints["manual_search_ai_agent_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if answer_recommendation_ai_agent_configuration is not None:
                self._values["answer_recommendation_ai_agent_configuration"] = answer_recommendation_ai_agent_configuration
            if manual_search_ai_agent_configuration is not None:
                self._values["manual_search_ai_agent_configuration"] = manual_search_ai_agent_configuration

        @builtins.property
        def answer_recommendation_ai_agent_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAIAgent.AnswerRecommendationAIAgentConfigurationProperty"]]:
            '''The configuration for AI Agents of type ``ANSWER_RECOMMENDATION`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-aiagentconfiguration.html#cfn-wisdom-aiagent-aiagentconfiguration-answerrecommendationaiagentconfiguration
            '''
            result = self._values.get("answer_recommendation_ai_agent_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAIAgent.AnswerRecommendationAIAgentConfigurationProperty"]], result)

        @builtins.property
        def manual_search_ai_agent_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAIAgent.ManualSearchAIAgentConfigurationProperty"]]:
            '''The configuration for AI Agents of type ``MANUAL_SEARCH`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-aiagentconfiguration.html#cfn-wisdom-aiagent-aiagentconfiguration-manualsearchaiagentconfiguration
            '''
            result = self._values.get("manual_search_ai_agent_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAIAgent.ManualSearchAIAgentConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AIAgentConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnAIAgent.AnswerRecommendationAIAgentConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "answer_generation_ai_prompt_id": "answerGenerationAiPromptId",
            "association_configurations": "associationConfigurations",
            "intent_labeling_generation_ai_prompt_id": "intentLabelingGenerationAiPromptId",
            "query_reformulation_ai_prompt_id": "queryReformulationAiPromptId",
        },
    )
    class AnswerRecommendationAIAgentConfigurationProperty:
        def __init__(
            self,
            *,
            answer_generation_ai_prompt_id: typing.Optional[builtins.str] = None,
            association_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAIAgent.AssociationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            intent_labeling_generation_ai_prompt_id: typing.Optional[builtins.str] = None,
            query_reformulation_ai_prompt_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configuration for AI Agents of type ``ANSWER_RECOMMENDATION`` .

            :param answer_generation_ai_prompt_id: The AI Prompt identifier for the Answer Generation prompt used by the ``ANSWER_RECOMMENDATION`` AI Agent.
            :param association_configurations: The association configurations for overriding behavior on this AI Agent.
            :param intent_labeling_generation_ai_prompt_id: The AI Prompt identifier for the Intent Labeling prompt used by the ``ANSWER_RECOMMENDATION`` AI Agent.
            :param query_reformulation_ai_prompt_id: The AI Prompt identifier for the Query Reformulation prompt used by the ``ANSWER_RECOMMENDATION`` AI Agent.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-answerrecommendationaiagentconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                answer_recommendation_aIAgent_configuration_property = wisdom.CfnAIAgent.AnswerRecommendationAIAgentConfigurationProperty(
                    answer_generation_ai_prompt_id="answerGenerationAiPromptId",
                    association_configurations=[wisdom.CfnAIAgent.AssociationConfigurationProperty(
                        association_configuration_data=wisdom.CfnAIAgent.AssociationConfigurationDataProperty(
                            knowledge_base_association_configuration_data=wisdom.CfnAIAgent.KnowledgeBaseAssociationConfigurationDataProperty(
                                content_tag_filter=wisdom.CfnAIAgent.TagFilterProperty(
                                    and_conditions=[wisdom.CfnAIAgent.TagConditionProperty(
                                        key="key",
                
                                        # the properties below are optional
                                        value="value"
                                    )],
                                    or_conditions=[wisdom.CfnAIAgent.OrConditionProperty(
                                        and_conditions=[wisdom.CfnAIAgent.TagConditionProperty(
                                            key="key",
                
                                            # the properties below are optional
                                            value="value"
                                        )],
                                        tag_condition=wisdom.CfnAIAgent.TagConditionProperty(
                                            key="key",
                
                                            # the properties below are optional
                                            value="value"
                                        )
                                    )],
                                    tag_condition=wisdom.CfnAIAgent.TagConditionProperty(
                                        key="key",
                
                                        # the properties below are optional
                                        value="value"
                                    )
                                ),
                                max_results=123,
                                override_knowledge_base_search_type="overrideKnowledgeBaseSearchType"
                            )
                        ),
                        association_id="associationId",
                        association_type="associationType"
                    )],
                    intent_labeling_generation_ai_prompt_id="intentLabelingGenerationAiPromptId",
                    query_reformulation_ai_prompt_id="queryReformulationAiPromptId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6847cf788b7def362d576a512b579b2a08c25837003298b7c57254d1dfb45112)
                check_type(argname="argument answer_generation_ai_prompt_id", value=answer_generation_ai_prompt_id, expected_type=type_hints["answer_generation_ai_prompt_id"])
                check_type(argname="argument association_configurations", value=association_configurations, expected_type=type_hints["association_configurations"])
                check_type(argname="argument intent_labeling_generation_ai_prompt_id", value=intent_labeling_generation_ai_prompt_id, expected_type=type_hints["intent_labeling_generation_ai_prompt_id"])
                check_type(argname="argument query_reformulation_ai_prompt_id", value=query_reformulation_ai_prompt_id, expected_type=type_hints["query_reformulation_ai_prompt_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if answer_generation_ai_prompt_id is not None:
                self._values["answer_generation_ai_prompt_id"] = answer_generation_ai_prompt_id
            if association_configurations is not None:
                self._values["association_configurations"] = association_configurations
            if intent_labeling_generation_ai_prompt_id is not None:
                self._values["intent_labeling_generation_ai_prompt_id"] = intent_labeling_generation_ai_prompt_id
            if query_reformulation_ai_prompt_id is not None:
                self._values["query_reformulation_ai_prompt_id"] = query_reformulation_ai_prompt_id

        @builtins.property
        def answer_generation_ai_prompt_id(self) -> typing.Optional[builtins.str]:
            '''The AI Prompt identifier for the Answer Generation prompt used by the ``ANSWER_RECOMMENDATION`` AI Agent.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-answerrecommendationaiagentconfiguration.html#cfn-wisdom-aiagent-answerrecommendationaiagentconfiguration-answergenerationaipromptid
            '''
            result = self._values.get("answer_generation_ai_prompt_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def association_configurations(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAIAgent.AssociationConfigurationProperty"]]]]:
            '''The association configurations for overriding behavior on this AI Agent.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-answerrecommendationaiagentconfiguration.html#cfn-wisdom-aiagent-answerrecommendationaiagentconfiguration-associationconfigurations
            '''
            result = self._values.get("association_configurations")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAIAgent.AssociationConfigurationProperty"]]]], result)

        @builtins.property
        def intent_labeling_generation_ai_prompt_id(
            self,
        ) -> typing.Optional[builtins.str]:
            '''The AI Prompt identifier for the Intent Labeling prompt used by the ``ANSWER_RECOMMENDATION`` AI Agent.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-answerrecommendationaiagentconfiguration.html#cfn-wisdom-aiagent-answerrecommendationaiagentconfiguration-intentlabelinggenerationaipromptid
            '''
            result = self._values.get("intent_labeling_generation_ai_prompt_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def query_reformulation_ai_prompt_id(self) -> typing.Optional[builtins.str]:
            '''The AI Prompt identifier for the Query Reformulation prompt used by the ``ANSWER_RECOMMENDATION`` AI Agent.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-answerrecommendationaiagentconfiguration.html#cfn-wisdom-aiagent-answerrecommendationaiagentconfiguration-queryreformulationaipromptid
            '''
            result = self._values.get("query_reformulation_ai_prompt_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AnswerRecommendationAIAgentConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnAIAgent.AssociationConfigurationDataProperty",
        jsii_struct_bases=[],
        name_mapping={
            "knowledge_base_association_configuration_data": "knowledgeBaseAssociationConfigurationData",
        },
    )
    class AssociationConfigurationDataProperty:
        def __init__(
            self,
            *,
            knowledge_base_association_configuration_data: typing.Union[_IResolvable_da3f097b, typing.Union["CfnAIAgent.KnowledgeBaseAssociationConfigurationDataProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''A typed union of the data of the configuration for an Amazon Q in Connect Assistant Association.

            :param knowledge_base_association_configuration_data: The data of the configuration for a ``KNOWLEDGE_BASE`` type Amazon Q in Connect Assistant Association.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-associationconfigurationdata.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                association_configuration_data_property = wisdom.CfnAIAgent.AssociationConfigurationDataProperty(
                    knowledge_base_association_configuration_data=wisdom.CfnAIAgent.KnowledgeBaseAssociationConfigurationDataProperty(
                        content_tag_filter=wisdom.CfnAIAgent.TagFilterProperty(
                            and_conditions=[wisdom.CfnAIAgent.TagConditionProperty(
                                key="key",
                
                                # the properties below are optional
                                value="value"
                            )],
                            or_conditions=[wisdom.CfnAIAgent.OrConditionProperty(
                                and_conditions=[wisdom.CfnAIAgent.TagConditionProperty(
                                    key="key",
                
                                    # the properties below are optional
                                    value="value"
                                )],
                                tag_condition=wisdom.CfnAIAgent.TagConditionProperty(
                                    key="key",
                
                                    # the properties below are optional
                                    value="value"
                                )
                            )],
                            tag_condition=wisdom.CfnAIAgent.TagConditionProperty(
                                key="key",
                
                                # the properties below are optional
                                value="value"
                            )
                        ),
                        max_results=123,
                        override_knowledge_base_search_type="overrideKnowledgeBaseSearchType"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c351d3e3386a19a82d6920c115ac6f8c911a12da4a117a9c0676a8ff0038fd41)
                check_type(argname="argument knowledge_base_association_configuration_data", value=knowledge_base_association_configuration_data, expected_type=type_hints["knowledge_base_association_configuration_data"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "knowledge_base_association_configuration_data": knowledge_base_association_configuration_data,
            }

        @builtins.property
        def knowledge_base_association_configuration_data(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnAIAgent.KnowledgeBaseAssociationConfigurationDataProperty"]:
            '''The data of the configuration for a ``KNOWLEDGE_BASE`` type Amazon Q in Connect Assistant Association.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-associationconfigurationdata.html#cfn-wisdom-aiagent-associationconfigurationdata-knowledgebaseassociationconfigurationdata
            '''
            result = self._values.get("knowledge_base_association_configuration_data")
            assert result is not None, "Required property 'knowledge_base_association_configuration_data' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnAIAgent.KnowledgeBaseAssociationConfigurationDataProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AssociationConfigurationDataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnAIAgent.AssociationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "association_configuration_data": "associationConfigurationData",
            "association_id": "associationId",
            "association_type": "associationType",
        },
    )
    class AssociationConfigurationProperty:
        def __init__(
            self,
            *,
            association_configuration_data: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAIAgent.AssociationConfigurationDataProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            association_id: typing.Optional[builtins.str] = None,
            association_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configuration for an Amazon Q in Connect Assistant Association.

            :param association_configuration_data: A typed union of the data of the configuration for an Amazon Q in Connect Assistant Association.
            :param association_id: The identifier of the association for this Association Configuration.
            :param association_type: The type of the association for this Association Configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-associationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                association_configuration_property = wisdom.CfnAIAgent.AssociationConfigurationProperty(
                    association_configuration_data=wisdom.CfnAIAgent.AssociationConfigurationDataProperty(
                        knowledge_base_association_configuration_data=wisdom.CfnAIAgent.KnowledgeBaseAssociationConfigurationDataProperty(
                            content_tag_filter=wisdom.CfnAIAgent.TagFilterProperty(
                                and_conditions=[wisdom.CfnAIAgent.TagConditionProperty(
                                    key="key",
                
                                    # the properties below are optional
                                    value="value"
                                )],
                                or_conditions=[wisdom.CfnAIAgent.OrConditionProperty(
                                    and_conditions=[wisdom.CfnAIAgent.TagConditionProperty(
                                        key="key",
                
                                        # the properties below are optional
                                        value="value"
                                    )],
                                    tag_condition=wisdom.CfnAIAgent.TagConditionProperty(
                                        key="key",
                
                                        # the properties below are optional
                                        value="value"
                                    )
                                )],
                                tag_condition=wisdom.CfnAIAgent.TagConditionProperty(
                                    key="key",
                
                                    # the properties below are optional
                                    value="value"
                                )
                            ),
                            max_results=123,
                            override_knowledge_base_search_type="overrideKnowledgeBaseSearchType"
                        )
                    ),
                    association_id="associationId",
                    association_type="associationType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2df56062b7b8c55a883d0469e63c3aad05d8079bf21171f13f4e68d2f26fea44)
                check_type(argname="argument association_configuration_data", value=association_configuration_data, expected_type=type_hints["association_configuration_data"])
                check_type(argname="argument association_id", value=association_id, expected_type=type_hints["association_id"])
                check_type(argname="argument association_type", value=association_type, expected_type=type_hints["association_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if association_configuration_data is not None:
                self._values["association_configuration_data"] = association_configuration_data
            if association_id is not None:
                self._values["association_id"] = association_id
            if association_type is not None:
                self._values["association_type"] = association_type

        @builtins.property
        def association_configuration_data(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAIAgent.AssociationConfigurationDataProperty"]]:
            '''A typed union of the data of the configuration for an Amazon Q in Connect Assistant Association.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-associationconfiguration.html#cfn-wisdom-aiagent-associationconfiguration-associationconfigurationdata
            '''
            result = self._values.get("association_configuration_data")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAIAgent.AssociationConfigurationDataProperty"]], result)

        @builtins.property
        def association_id(self) -> typing.Optional[builtins.str]:
            '''The identifier of the association for this Association Configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-associationconfiguration.html#cfn-wisdom-aiagent-associationconfiguration-associationid
            '''
            result = self._values.get("association_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def association_type(self) -> typing.Optional[builtins.str]:
            '''The type of the association for this Association Configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-associationconfiguration.html#cfn-wisdom-aiagent-associationconfiguration-associationtype
            '''
            result = self._values.get("association_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AssociationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnAIAgent.KnowledgeBaseAssociationConfigurationDataProperty",
        jsii_struct_bases=[],
        name_mapping={
            "content_tag_filter": "contentTagFilter",
            "max_results": "maxResults",
            "override_knowledge_base_search_type": "overrideKnowledgeBaseSearchType",
        },
    )
    class KnowledgeBaseAssociationConfigurationDataProperty:
        def __init__(
            self,
            *,
            content_tag_filter: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAIAgent.TagFilterProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            max_results: typing.Optional[jsii.Number] = None,
            override_knowledge_base_search_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The data of the configuration for a ``KNOWLEDGE_BASE`` type Amazon Q in Connect Assistant Association.

            :param content_tag_filter: An object that can be used to specify Tag conditions.
            :param max_results: The maximum number of results to return per page.
            :param override_knowledge_base_search_type: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-knowledgebaseassociationconfigurationdata.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                knowledge_base_association_configuration_data_property = wisdom.CfnAIAgent.KnowledgeBaseAssociationConfigurationDataProperty(
                    content_tag_filter=wisdom.CfnAIAgent.TagFilterProperty(
                        and_conditions=[wisdom.CfnAIAgent.TagConditionProperty(
                            key="key",
                
                            # the properties below are optional
                            value="value"
                        )],
                        or_conditions=[wisdom.CfnAIAgent.OrConditionProperty(
                            and_conditions=[wisdom.CfnAIAgent.TagConditionProperty(
                                key="key",
                
                                # the properties below are optional
                                value="value"
                            )],
                            tag_condition=wisdom.CfnAIAgent.TagConditionProperty(
                                key="key",
                
                                # the properties below are optional
                                value="value"
                            )
                        )],
                        tag_condition=wisdom.CfnAIAgent.TagConditionProperty(
                            key="key",
                
                            # the properties below are optional
                            value="value"
                        )
                    ),
                    max_results=123,
                    override_knowledge_base_search_type="overrideKnowledgeBaseSearchType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__af25ecdf7592033a618b9a411d145fb2bd7b10ae3e9b0a04a4502e0dee139e27)
                check_type(argname="argument content_tag_filter", value=content_tag_filter, expected_type=type_hints["content_tag_filter"])
                check_type(argname="argument max_results", value=max_results, expected_type=type_hints["max_results"])
                check_type(argname="argument override_knowledge_base_search_type", value=override_knowledge_base_search_type, expected_type=type_hints["override_knowledge_base_search_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if content_tag_filter is not None:
                self._values["content_tag_filter"] = content_tag_filter
            if max_results is not None:
                self._values["max_results"] = max_results
            if override_knowledge_base_search_type is not None:
                self._values["override_knowledge_base_search_type"] = override_knowledge_base_search_type

        @builtins.property
        def content_tag_filter(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAIAgent.TagFilterProperty"]]:
            '''An object that can be used to specify Tag conditions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-knowledgebaseassociationconfigurationdata.html#cfn-wisdom-aiagent-knowledgebaseassociationconfigurationdata-contenttagfilter
            '''
            result = self._values.get("content_tag_filter")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAIAgent.TagFilterProperty"]], result)

        @builtins.property
        def max_results(self) -> typing.Optional[jsii.Number]:
            '''The maximum number of results to return per page.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-knowledgebaseassociationconfigurationdata.html#cfn-wisdom-aiagent-knowledgebaseassociationconfigurationdata-maxresults
            '''
            result = self._values.get("max_results")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def override_knowledge_base_search_type(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-knowledgebaseassociationconfigurationdata.html#cfn-wisdom-aiagent-knowledgebaseassociationconfigurationdata-overrideknowledgebasesearchtype
            '''
            result = self._values.get("override_knowledge_base_search_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KnowledgeBaseAssociationConfigurationDataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnAIAgent.ManualSearchAIAgentConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "answer_generation_ai_prompt_id": "answerGenerationAiPromptId",
            "association_configurations": "associationConfigurations",
        },
    )
    class ManualSearchAIAgentConfigurationProperty:
        def __init__(
            self,
            *,
            answer_generation_ai_prompt_id: typing.Optional[builtins.str] = None,
            association_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAIAgent.AssociationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''The configuration for AI Agents of type ``MANUAL_SEARCH`` .

            :param answer_generation_ai_prompt_id: The AI Prompt identifier for the Answer Generation prompt used by the ``ANSWER_RECOMMENDATION`` AI Agent.
            :param association_configurations: The association configurations for overriding behavior on this AI Agent.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-manualsearchaiagentconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                manual_search_aIAgent_configuration_property = wisdom.CfnAIAgent.ManualSearchAIAgentConfigurationProperty(
                    answer_generation_ai_prompt_id="answerGenerationAiPromptId",
                    association_configurations=[wisdom.CfnAIAgent.AssociationConfigurationProperty(
                        association_configuration_data=wisdom.CfnAIAgent.AssociationConfigurationDataProperty(
                            knowledge_base_association_configuration_data=wisdom.CfnAIAgent.KnowledgeBaseAssociationConfigurationDataProperty(
                                content_tag_filter=wisdom.CfnAIAgent.TagFilterProperty(
                                    and_conditions=[wisdom.CfnAIAgent.TagConditionProperty(
                                        key="key",
                
                                        # the properties below are optional
                                        value="value"
                                    )],
                                    or_conditions=[wisdom.CfnAIAgent.OrConditionProperty(
                                        and_conditions=[wisdom.CfnAIAgent.TagConditionProperty(
                                            key="key",
                
                                            # the properties below are optional
                                            value="value"
                                        )],
                                        tag_condition=wisdom.CfnAIAgent.TagConditionProperty(
                                            key="key",
                
                                            # the properties below are optional
                                            value="value"
                                        )
                                    )],
                                    tag_condition=wisdom.CfnAIAgent.TagConditionProperty(
                                        key="key",
                
                                        # the properties below are optional
                                        value="value"
                                    )
                                ),
                                max_results=123,
                                override_knowledge_base_search_type="overrideKnowledgeBaseSearchType"
                            )
                        ),
                        association_id="associationId",
                        association_type="associationType"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3346eba3a05ad4b31350bf2c54edbb6063a18cfea8a25ebbab80c402438f039a)
                check_type(argname="argument answer_generation_ai_prompt_id", value=answer_generation_ai_prompt_id, expected_type=type_hints["answer_generation_ai_prompt_id"])
                check_type(argname="argument association_configurations", value=association_configurations, expected_type=type_hints["association_configurations"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if answer_generation_ai_prompt_id is not None:
                self._values["answer_generation_ai_prompt_id"] = answer_generation_ai_prompt_id
            if association_configurations is not None:
                self._values["association_configurations"] = association_configurations

        @builtins.property
        def answer_generation_ai_prompt_id(self) -> typing.Optional[builtins.str]:
            '''The AI Prompt identifier for the Answer Generation prompt used by the ``ANSWER_RECOMMENDATION`` AI Agent.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-manualsearchaiagentconfiguration.html#cfn-wisdom-aiagent-manualsearchaiagentconfiguration-answergenerationaipromptid
            '''
            result = self._values.get("answer_generation_ai_prompt_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def association_configurations(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAIAgent.AssociationConfigurationProperty"]]]]:
            '''The association configurations for overriding behavior on this AI Agent.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-manualsearchaiagentconfiguration.html#cfn-wisdom-aiagent-manualsearchaiagentconfiguration-associationconfigurations
            '''
            result = self._values.get("association_configurations")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAIAgent.AssociationConfigurationProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ManualSearchAIAgentConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnAIAgent.OrConditionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "and_conditions": "andConditions",
            "tag_condition": "tagCondition",
        },
    )
    class OrConditionProperty:
        def __init__(
            self,
            *,
            and_conditions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAIAgent.TagConditionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            tag_condition: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAIAgent.TagConditionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param and_conditions: 
            :param tag_condition: A leaf node condition which can be used to specify a tag condition.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-orcondition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                or_condition_property = wisdom.CfnAIAgent.OrConditionProperty(
                    and_conditions=[wisdom.CfnAIAgent.TagConditionProperty(
                        key="key",
                
                        # the properties below are optional
                        value="value"
                    )],
                    tag_condition=wisdom.CfnAIAgent.TagConditionProperty(
                        key="key",
                
                        # the properties below are optional
                        value="value"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bf2bbad68aea63c5546563872782e30b131382ddae5fbabf04602b928494d4d4)
                check_type(argname="argument and_conditions", value=and_conditions, expected_type=type_hints["and_conditions"])
                check_type(argname="argument tag_condition", value=tag_condition, expected_type=type_hints["tag_condition"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if and_conditions is not None:
                self._values["and_conditions"] = and_conditions
            if tag_condition is not None:
                self._values["tag_condition"] = tag_condition

        @builtins.property
        def and_conditions(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAIAgent.TagConditionProperty"]]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-orcondition.html#cfn-wisdom-aiagent-orcondition-andconditions
            '''
            result = self._values.get("and_conditions")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAIAgent.TagConditionProperty"]]]], result)

        @builtins.property
        def tag_condition(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAIAgent.TagConditionProperty"]]:
            '''A leaf node condition which can be used to specify a tag condition.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-orcondition.html#cfn-wisdom-aiagent-orcondition-tagcondition
            '''
            result = self._values.get("tag_condition")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAIAgent.TagConditionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OrConditionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnAIAgent.TagConditionProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class TagConditionProperty:
        def __init__(
            self,
            *,
            key: builtins.str,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An object that can be used to specify tag conditions.

            :param key: The tag key in the tag condition.
            :param value: The tag value in the tag condition.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-tagcondition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                tag_condition_property = wisdom.CfnAIAgent.TagConditionProperty(
                    key="key",
                
                    # the properties below are optional
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__76535774a57202e416fb208d73c095c91408f65fd8a1b99f6b568fd994b915e9)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
            }
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def key(self) -> builtins.str:
            '''The tag key in the tag condition.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-tagcondition.html#cfn-wisdom-aiagent-tagcondition-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''The tag value in the tag condition.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-tagcondition.html#cfn-wisdom-aiagent-tagcondition-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TagConditionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnAIAgent.TagFilterProperty",
        jsii_struct_bases=[],
        name_mapping={
            "and_conditions": "andConditions",
            "or_conditions": "orConditions",
            "tag_condition": "tagCondition",
        },
    )
    class TagFilterProperty:
        def __init__(
            self,
            *,
            and_conditions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAIAgent.TagConditionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            or_conditions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAIAgent.OrConditionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            tag_condition: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAIAgent.TagConditionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''An object that can be used to specify tag conditions.

            :param and_conditions: A list of conditions which would be applied together with an ``AND`` condition.
            :param or_conditions: A list of conditions which would be applied together with an ``OR`` condition.
            :param tag_condition: A leaf node condition which can be used to specify a tag condition.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-tagfilter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                tag_filter_property = wisdom.CfnAIAgent.TagFilterProperty(
                    and_conditions=[wisdom.CfnAIAgent.TagConditionProperty(
                        key="key",
                
                        # the properties below are optional
                        value="value"
                    )],
                    or_conditions=[wisdom.CfnAIAgent.OrConditionProperty(
                        and_conditions=[wisdom.CfnAIAgent.TagConditionProperty(
                            key="key",
                
                            # the properties below are optional
                            value="value"
                        )],
                        tag_condition=wisdom.CfnAIAgent.TagConditionProperty(
                            key="key",
                
                            # the properties below are optional
                            value="value"
                        )
                    )],
                    tag_condition=wisdom.CfnAIAgent.TagConditionProperty(
                        key="key",
                
                        # the properties below are optional
                        value="value"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__47961a691b994d09a0537dc7d655a0aab653585a5e8bd78b30c4bc84ec243c19)
                check_type(argname="argument and_conditions", value=and_conditions, expected_type=type_hints["and_conditions"])
                check_type(argname="argument or_conditions", value=or_conditions, expected_type=type_hints["or_conditions"])
                check_type(argname="argument tag_condition", value=tag_condition, expected_type=type_hints["tag_condition"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if and_conditions is not None:
                self._values["and_conditions"] = and_conditions
            if or_conditions is not None:
                self._values["or_conditions"] = or_conditions
            if tag_condition is not None:
                self._values["tag_condition"] = tag_condition

        @builtins.property
        def and_conditions(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAIAgent.TagConditionProperty"]]]]:
            '''A list of conditions which would be applied together with an ``AND`` condition.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-tagfilter.html#cfn-wisdom-aiagent-tagfilter-andconditions
            '''
            result = self._values.get("and_conditions")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAIAgent.TagConditionProperty"]]]], result)

        @builtins.property
        def or_conditions(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAIAgent.OrConditionProperty"]]]]:
            '''A list of conditions which would be applied together with an ``OR`` condition.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-tagfilter.html#cfn-wisdom-aiagent-tagfilter-orconditions
            '''
            result = self._values.get("or_conditions")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAIAgent.OrConditionProperty"]]]], result)

        @builtins.property
        def tag_condition(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAIAgent.TagConditionProperty"]]:
            '''A leaf node condition which can be used to specify a tag condition.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-tagfilter.html#cfn-wisdom-aiagent-tagfilter-tagcondition
            '''
            result = self._values.get("tag_condition")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAIAgent.TagConditionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TagFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_wisdom.CfnAIAgentProps",
    jsii_struct_bases=[],
    name_mapping={
        "assistant_id": "assistantId",
        "configuration": "configuration",
        "type": "type",
        "description": "description",
        "name": "name",
        "tags": "tags",
    },
)
class CfnAIAgentProps:
    def __init__(
        self,
        *,
        assistant_id: builtins.str,
        configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIAgent.AIAgentConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnAIAgent``.

        :param assistant_id: The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
        :param configuration: Configuration for the AI Agent.
        :param type: The type of the AI Agent.
        :param description: The description of the AI Agent.
        :param name: The name of the AI Agent.
        :param tags: The tags used to organize, track, or control access for this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiagent.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_wisdom as wisdom
            
            cfn_aIAgent_props = wisdom.CfnAIAgentProps(
                assistant_id="assistantId",
                configuration=wisdom.CfnAIAgent.AIAgentConfigurationProperty(
                    answer_recommendation_ai_agent_configuration=wisdom.CfnAIAgent.AnswerRecommendationAIAgentConfigurationProperty(
                        answer_generation_ai_prompt_id="answerGenerationAiPromptId",
                        association_configurations=[wisdom.CfnAIAgent.AssociationConfigurationProperty(
                            association_configuration_data=wisdom.CfnAIAgent.AssociationConfigurationDataProperty(
                                knowledge_base_association_configuration_data=wisdom.CfnAIAgent.KnowledgeBaseAssociationConfigurationDataProperty(
                                    content_tag_filter=wisdom.CfnAIAgent.TagFilterProperty(
                                        and_conditions=[wisdom.CfnAIAgent.TagConditionProperty(
                                            key="key",
            
                                            # the properties below are optional
                                            value="value"
                                        )],
                                        or_conditions=[wisdom.CfnAIAgent.OrConditionProperty(
                                            and_conditions=[wisdom.CfnAIAgent.TagConditionProperty(
                                                key="key",
            
                                                # the properties below are optional
                                                value="value"
                                            )],
                                            tag_condition=wisdom.CfnAIAgent.TagConditionProperty(
                                                key="key",
            
                                                # the properties below are optional
                                                value="value"
                                            )
                                        )],
                                        tag_condition=wisdom.CfnAIAgent.TagConditionProperty(
                                            key="key",
            
                                            # the properties below are optional
                                            value="value"
                                        )
                                    ),
                                    max_results=123,
                                    override_knowledge_base_search_type="overrideKnowledgeBaseSearchType"
                                )
                            ),
                            association_id="associationId",
                            association_type="associationType"
                        )],
                        intent_labeling_generation_ai_prompt_id="intentLabelingGenerationAiPromptId",
                        query_reformulation_ai_prompt_id="queryReformulationAiPromptId"
                    ),
                    manual_search_ai_agent_configuration=wisdom.CfnAIAgent.ManualSearchAIAgentConfigurationProperty(
                        answer_generation_ai_prompt_id="answerGenerationAiPromptId",
                        association_configurations=[wisdom.CfnAIAgent.AssociationConfigurationProperty(
                            association_configuration_data=wisdom.CfnAIAgent.AssociationConfigurationDataProperty(
                                knowledge_base_association_configuration_data=wisdom.CfnAIAgent.KnowledgeBaseAssociationConfigurationDataProperty(
                                    content_tag_filter=wisdom.CfnAIAgent.TagFilterProperty(
                                        and_conditions=[wisdom.CfnAIAgent.TagConditionProperty(
                                            key="key",
            
                                            # the properties below are optional
                                            value="value"
                                        )],
                                        or_conditions=[wisdom.CfnAIAgent.OrConditionProperty(
                                            and_conditions=[wisdom.CfnAIAgent.TagConditionProperty(
                                                key="key",
            
                                                # the properties below are optional
                                                value="value"
                                            )],
                                            tag_condition=wisdom.CfnAIAgent.TagConditionProperty(
                                                key="key",
            
                                                # the properties below are optional
                                                value="value"
                                            )
                                        )],
                                        tag_condition=wisdom.CfnAIAgent.TagConditionProperty(
                                            key="key",
            
                                            # the properties below are optional
                                            value="value"
                                        )
                                    ),
                                    max_results=123,
                                    override_knowledge_base_search_type="overrideKnowledgeBaseSearchType"
                                )
                            ),
                            association_id="associationId",
                            association_type="associationType"
                        )]
                    )
                ),
                type="type",
            
                # the properties below are optional
                description="description",
                name="name",
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1cda9a6282ec07c28c0ef49efdf8da8f079052d26edd32bbe15324644982756)
            check_type(argname="argument assistant_id", value=assistant_id, expected_type=type_hints["assistant_id"])
            check_type(argname="argument configuration", value=configuration, expected_type=type_hints["configuration"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "assistant_id": assistant_id,
            "configuration": configuration,
            "type": type,
        }
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def assistant_id(self) -> builtins.str:
        '''The identifier of the Amazon Q in Connect assistant.

        Can be either the ID or the ARN. URLs cannot contain the ARN.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiagent.html#cfn-wisdom-aiagent-assistantid
        '''
        result = self._values.get("assistant_id")
        assert result is not None, "Required property 'assistant_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnAIAgent.AIAgentConfigurationProperty]:
        '''Configuration for the AI Agent.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiagent.html#cfn-wisdom-aiagent-configuration
        '''
        result = self._values.get("configuration")
        assert result is not None, "Required property 'configuration' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnAIAgent.AIAgentConfigurationProperty], result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of the AI Agent.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiagent.html#cfn-wisdom-aiagent-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the AI Agent.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiagent.html#cfn-wisdom-aiagent-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the AI Agent.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiagent.html#cfn-wisdom-aiagent-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags used to organize, track, or control access for this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiagent.html#cfn-wisdom-aiagent-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAIAgentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnAIAgentVersion(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_wisdom.CfnAIAgentVersion",
):
    '''Creates and Amazon Q in Connect AI Agent version.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiagentversion.html
    :cloudformationResource: AWS::Wisdom::AIAgentVersion
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_wisdom as wisdom
        
        cfn_aIAgent_version = wisdom.CfnAIAgentVersion(self, "MyCfnAIAgentVersion",
            ai_agent_id="aiAgentId",
            assistant_id="assistantId",
        
            # the properties below are optional
            modified_time_seconds=123
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        ai_agent_id: builtins.str,
        assistant_id: builtins.str,
        modified_time_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param ai_agent_id: The identifier of the AI Agent.
        :param assistant_id: 
        :param modified_time_seconds: The time the AI Agent version was last modified in seconds.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa5a166c3d658d9410f80c3ff44a4aee88b29cb4def5f6c7d811c5b47f5ffb68)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAIAgentVersionProps(
            ai_agent_id=ai_agent_id,
            assistant_id=assistant_id,
            modified_time_seconds=modified_time_seconds,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eec3c0a8aee757b615051ab77f3708fef64acd48758d58f7b8801c7073f3ea55)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1eec2d46406b6deb09ae2fc5f30e9bb5223c8f293091f02f7d13f928906953a1)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAiAgentArn")
    def attr_ai_agent_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: AIAgentArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAiAgentArn"))

    @builtins.property
    @jsii.member(jsii_name="attrAiAgentVersionId")
    def attr_ai_agent_version_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: AIAgentVersionId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAiAgentVersionId"))

    @builtins.property
    @jsii.member(jsii_name="attrAssistantArn")
    def attr_assistant_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: AssistantArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAssistantArn"))

    @builtins.property
    @jsii.member(jsii_name="attrVersionNumber")
    def attr_version_number(self) -> _IResolvable_da3f097b:
        '''The version number for this AI Agent version.

        :cloudformationAttribute: VersionNumber
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrVersionNumber"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="aiAgentId")
    def ai_agent_id(self) -> builtins.str:
        '''The identifier of the AI Agent.'''
        return typing.cast(builtins.str, jsii.get(self, "aiAgentId"))

    @ai_agent_id.setter
    def ai_agent_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df356486e6fdad853cdc4c3aa5d62a5febffd1441d8e82f3a672bf4aef6e809d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aiAgentId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="assistantId")
    def assistant_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "assistantId"))

    @assistant_id.setter
    def assistant_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3c00eedc618755e116ec4cf13129b9ecab51c03e0aa3285aa6c4eca0e7c9311)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assistantId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="modifiedTimeSeconds")
    def modified_time_seconds(self) -> typing.Optional[jsii.Number]:
        '''The time the AI Agent version was last modified in seconds.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "modifiedTimeSeconds"))

    @modified_time_seconds.setter
    def modified_time_seconds(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1cbb04d6951221f1cfd98bc4ebed42ba72b9f79a3ef0707bfcea622572f06cd2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "modifiedTimeSeconds", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_wisdom.CfnAIAgentVersionProps",
    jsii_struct_bases=[],
    name_mapping={
        "ai_agent_id": "aiAgentId",
        "assistant_id": "assistantId",
        "modified_time_seconds": "modifiedTimeSeconds",
    },
)
class CfnAIAgentVersionProps:
    def __init__(
        self,
        *,
        ai_agent_id: builtins.str,
        assistant_id: builtins.str,
        modified_time_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Properties for defining a ``CfnAIAgentVersion``.

        :param ai_agent_id: The identifier of the AI Agent.
        :param assistant_id: 
        :param modified_time_seconds: The time the AI Agent version was last modified in seconds.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiagentversion.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_wisdom as wisdom
            
            cfn_aIAgent_version_props = wisdom.CfnAIAgentVersionProps(
                ai_agent_id="aiAgentId",
                assistant_id="assistantId",
            
                # the properties below are optional
                modified_time_seconds=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ce55b0c69b9bc58cfcaeadaff04d7986170a5f73af9f6157ba1fe19c79b250e)
            check_type(argname="argument ai_agent_id", value=ai_agent_id, expected_type=type_hints["ai_agent_id"])
            check_type(argname="argument assistant_id", value=assistant_id, expected_type=type_hints["assistant_id"])
            check_type(argname="argument modified_time_seconds", value=modified_time_seconds, expected_type=type_hints["modified_time_seconds"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ai_agent_id": ai_agent_id,
            "assistant_id": assistant_id,
        }
        if modified_time_seconds is not None:
            self._values["modified_time_seconds"] = modified_time_seconds

    @builtins.property
    def ai_agent_id(self) -> builtins.str:
        '''The identifier of the AI Agent.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiagentversion.html#cfn-wisdom-aiagentversion-aiagentid
        '''
        result = self._values.get("ai_agent_id")
        assert result is not None, "Required property 'ai_agent_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def assistant_id(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiagentversion.html#cfn-wisdom-aiagentversion-assistantid
        '''
        result = self._values.get("assistant_id")
        assert result is not None, "Required property 'assistant_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def modified_time_seconds(self) -> typing.Optional[jsii.Number]:
        '''The time the AI Agent version was last modified in seconds.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiagentversion.html#cfn-wisdom-aiagentversion-modifiedtimeseconds
        '''
        result = self._values.get("modified_time_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAIAgentVersionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnAIPrompt(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_wisdom.CfnAIPrompt",
):
    '''Creates an Amazon Q in Connect AI Prompt.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiprompt.html
    :cloudformationResource: AWS::Wisdom::AIPrompt
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_wisdom as wisdom
        
        cfn_aIPrompt = wisdom.CfnAIPrompt(self, "MyCfnAIPrompt",
            api_format="apiFormat",
            model_id="modelId",
            template_configuration=wisdom.CfnAIPrompt.AIPromptTemplateConfigurationProperty(
                text_full_ai_prompt_edit_template_configuration=wisdom.CfnAIPrompt.TextFullAIPromptEditTemplateConfigurationProperty(
                    text="text"
                )
            ),
            template_type="templateType",
            type="type",
        
            # the properties below are optional
            assistant_id="assistantId",
            description="description",
            name="name",
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        api_format: builtins.str,
        model_id: builtins.str,
        template_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnAIPrompt.AIPromptTemplateConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        template_type: builtins.str,
        type: builtins.str,
        assistant_id: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param api_format: The API format used for this AI Prompt.
        :param model_id: The identifier of the model used for this AI Prompt. Model Ids supported are: ``CLAUDE_3_HAIKU_20240307_V1`` .
        :param template_configuration: The configuration of the prompt template for this AI Prompt.
        :param template_type: The type of the prompt template for this AI Prompt.
        :param type: The type of this AI Prompt.
        :param assistant_id: The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
        :param description: The description of the AI Prompt.
        :param name: The name of the AI Prompt.
        :param tags: The tags used to organize, track, or control access for this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48a265f7ec519ced4028dd8e69d5a1fe8ef89d36b11d693c968f74c8be6bb9df)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAIPromptProps(
            api_format=api_format,
            model_id=model_id,
            template_configuration=template_configuration,
            template_type=template_type,
            type=type,
            assistant_id=assistant_id,
            description=description,
            name=name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7567e2bb6113fabf7ae624801bcdbbfa2507650c0fcedb4572ac328601553fcc)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c65608208361b5449f96e9e897202e481d956b960bbccf8366c60dac3e4bd70)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAiPromptArn")
    def attr_ai_prompt_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the AI Prompt.

        :cloudformationAttribute: AIPromptArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAiPromptArn"))

    @builtins.property
    @jsii.member(jsii_name="attrAiPromptId")
    def attr_ai_prompt_id(self) -> builtins.str:
        '''The identifier of the Amazon Q in Connect AI prompt.

        :cloudformationAttribute: AIPromptId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAiPromptId"))

    @builtins.property
    @jsii.member(jsii_name="attrAssistantArn")
    def attr_assistant_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the Amazon Q in Connect assistant.

        :cloudformationAttribute: AssistantArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAssistantArn"))

    @builtins.property
    @jsii.member(jsii_name="cdkTagManager")
    def cdk_tag_manager(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "cdkTagManager"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="apiFormat")
    def api_format(self) -> builtins.str:
        '''The API format used for this AI Prompt.'''
        return typing.cast(builtins.str, jsii.get(self, "apiFormat"))

    @api_format.setter
    def api_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6643cec138a765effc7d182e3db5b09b1ddb19205b800c1f517cbed5e73488b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiFormat", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="modelId")
    def model_id(self) -> builtins.str:
        '''The identifier of the model used for this AI Prompt.'''
        return typing.cast(builtins.str, jsii.get(self, "modelId"))

    @model_id.setter
    def model_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be2ea2c4f381a43b0574cf9f6fdcace2ba70655e5f3ebd78fd5e8c4541b05982)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "modelId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="templateConfiguration")
    def template_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnAIPrompt.AIPromptTemplateConfigurationProperty"]:
        '''The configuration of the prompt template for this AI Prompt.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnAIPrompt.AIPromptTemplateConfigurationProperty"], jsii.get(self, "templateConfiguration"))

    @template_configuration.setter
    def template_configuration(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnAIPrompt.AIPromptTemplateConfigurationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5419aa0c5422844ff34f9fc9a194021532fa6ada449722bb2aa4b846530445ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "templateConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="templateType")
    def template_type(self) -> builtins.str:
        '''The type of the prompt template for this AI Prompt.'''
        return typing.cast(builtins.str, jsii.get(self, "templateType"))

    @template_type.setter
    def template_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e4b3aeb8d77c711927acf1f94798cc7b4e483f8fc8bc95ae0b322f2c18a51f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "templateType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''The type of this AI Prompt.'''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3f45400801eabea6672075f9e78a389daf48244d79b0b5601339aad9840939b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="assistantId")
    def assistant_id(self) -> typing.Optional[builtins.str]:
        '''The identifier of the Amazon Q in Connect assistant.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "assistantId"))

    @assistant_id.setter
    def assistant_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5634dda4bc6094fc31dbde0ffceab32283f49a381e6e026ed12c76738e89fe5e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assistantId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the AI Prompt.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4aab971aeb8e18c48f506a9f2350fb427745d11ff1d792a38763843c7c52200b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the AI Prompt.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c8237463d9724c409122f49c9b69b5a1e0f429714ecc37326da2fb2d24ac916)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags used to organize, track, or control access for this resource.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ebc135e5b323c7d3a33dd614d94d6bb8425982f46dc4aafee23df90fac59a460)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnAIPrompt.AIPromptTemplateConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "text_full_ai_prompt_edit_template_configuration": "textFullAiPromptEditTemplateConfiguration",
        },
    )
    class AIPromptTemplateConfigurationProperty:
        def __init__(
            self,
            *,
            text_full_ai_prompt_edit_template_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnAIPrompt.TextFullAIPromptEditTemplateConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''A typed union that specifies the configuration for a prompt template based on its type.

            :param text_full_ai_prompt_edit_template_configuration: The configuration for a prompt template that supports full textual prompt configuration using a YAML prompt.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiprompt-aiprompttemplateconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                a_iPrompt_template_configuration_property = wisdom.CfnAIPrompt.AIPromptTemplateConfigurationProperty(
                    text_full_ai_prompt_edit_template_configuration=wisdom.CfnAIPrompt.TextFullAIPromptEditTemplateConfigurationProperty(
                        text="text"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a5c009da191a8948caab2f589b801cb2b5b6bd6f17d15c830bfcc3eac735974e)
                check_type(argname="argument text_full_ai_prompt_edit_template_configuration", value=text_full_ai_prompt_edit_template_configuration, expected_type=type_hints["text_full_ai_prompt_edit_template_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "text_full_ai_prompt_edit_template_configuration": text_full_ai_prompt_edit_template_configuration,
            }

        @builtins.property
        def text_full_ai_prompt_edit_template_configuration(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnAIPrompt.TextFullAIPromptEditTemplateConfigurationProperty"]:
            '''The configuration for a prompt template that supports full textual prompt configuration using a YAML prompt.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiprompt-aiprompttemplateconfiguration.html#cfn-wisdom-aiprompt-aiprompttemplateconfiguration-textfullaipromptedittemplateconfiguration
            '''
            result = self._values.get("text_full_ai_prompt_edit_template_configuration")
            assert result is not None, "Required property 'text_full_ai_prompt_edit_template_configuration' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnAIPrompt.TextFullAIPromptEditTemplateConfigurationProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AIPromptTemplateConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnAIPrompt.TextFullAIPromptEditTemplateConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"text": "text"},
    )
    class TextFullAIPromptEditTemplateConfigurationProperty:
        def __init__(self, *, text: builtins.str) -> None:
            '''The configuration for a prompt template that supports full textual prompt configuration using a YAML prompt.

            :param text: The YAML text for the AI Prompt template.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiprompt-textfullaipromptedittemplateconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                text_full_aIPrompt_edit_template_configuration_property = wisdom.CfnAIPrompt.TextFullAIPromptEditTemplateConfigurationProperty(
                    text="text"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__aab519c6a13d7d17f031944b9ddc67f7d24074f5ba48e4816f1ba2dfd7883ffc)
                check_type(argname="argument text", value=text, expected_type=type_hints["text"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "text": text,
            }

        @builtins.property
        def text(self) -> builtins.str:
            '''The YAML text for the AI Prompt template.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiprompt-textfullaipromptedittemplateconfiguration.html#cfn-wisdom-aiprompt-textfullaipromptedittemplateconfiguration-text
            '''
            result = self._values.get("text")
            assert result is not None, "Required property 'text' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TextFullAIPromptEditTemplateConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_wisdom.CfnAIPromptProps",
    jsii_struct_bases=[],
    name_mapping={
        "api_format": "apiFormat",
        "model_id": "modelId",
        "template_configuration": "templateConfiguration",
        "template_type": "templateType",
        "type": "type",
        "assistant_id": "assistantId",
        "description": "description",
        "name": "name",
        "tags": "tags",
    },
)
class CfnAIPromptProps:
    def __init__(
        self,
        *,
        api_format: builtins.str,
        model_id: builtins.str,
        template_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIPrompt.AIPromptTemplateConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
        template_type: builtins.str,
        type: builtins.str,
        assistant_id: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnAIPrompt``.

        :param api_format: The API format used for this AI Prompt.
        :param model_id: The identifier of the model used for this AI Prompt. Model Ids supported are: ``CLAUDE_3_HAIKU_20240307_V1`` .
        :param template_configuration: The configuration of the prompt template for this AI Prompt.
        :param template_type: The type of the prompt template for this AI Prompt.
        :param type: The type of this AI Prompt.
        :param assistant_id: The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
        :param description: The description of the AI Prompt.
        :param name: The name of the AI Prompt.
        :param tags: The tags used to organize, track, or control access for this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiprompt.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_wisdom as wisdom
            
            cfn_aIPrompt_props = wisdom.CfnAIPromptProps(
                api_format="apiFormat",
                model_id="modelId",
                template_configuration=wisdom.CfnAIPrompt.AIPromptTemplateConfigurationProperty(
                    text_full_ai_prompt_edit_template_configuration=wisdom.CfnAIPrompt.TextFullAIPromptEditTemplateConfigurationProperty(
                        text="text"
                    )
                ),
                template_type="templateType",
                type="type",
            
                # the properties below are optional
                assistant_id="assistantId",
                description="description",
                name="name",
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a55de2153828f44950073a28af3416601dc1f09105d3fa9d8f1ec243b3822d3)
            check_type(argname="argument api_format", value=api_format, expected_type=type_hints["api_format"])
            check_type(argname="argument model_id", value=model_id, expected_type=type_hints["model_id"])
            check_type(argname="argument template_configuration", value=template_configuration, expected_type=type_hints["template_configuration"])
            check_type(argname="argument template_type", value=template_type, expected_type=type_hints["template_type"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument assistant_id", value=assistant_id, expected_type=type_hints["assistant_id"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_format": api_format,
            "model_id": model_id,
            "template_configuration": template_configuration,
            "template_type": template_type,
            "type": type,
        }
        if assistant_id is not None:
            self._values["assistant_id"] = assistant_id
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def api_format(self) -> builtins.str:
        '''The API format used for this AI Prompt.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiprompt.html#cfn-wisdom-aiprompt-apiformat
        '''
        result = self._values.get("api_format")
        assert result is not None, "Required property 'api_format' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def model_id(self) -> builtins.str:
        '''The identifier of the model used for this AI Prompt.

        Model Ids supported are: ``CLAUDE_3_HAIKU_20240307_V1`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiprompt.html#cfn-wisdom-aiprompt-modelid
        '''
        result = self._values.get("model_id")
        assert result is not None, "Required property 'model_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def template_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnAIPrompt.AIPromptTemplateConfigurationProperty]:
        '''The configuration of the prompt template for this AI Prompt.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiprompt.html#cfn-wisdom-aiprompt-templateconfiguration
        '''
        result = self._values.get("template_configuration")
        assert result is not None, "Required property 'template_configuration' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnAIPrompt.AIPromptTemplateConfigurationProperty], result)

    @builtins.property
    def template_type(self) -> builtins.str:
        '''The type of the prompt template for this AI Prompt.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiprompt.html#cfn-wisdom-aiprompt-templatetype
        '''
        result = self._values.get("template_type")
        assert result is not None, "Required property 'template_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of this AI Prompt.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiprompt.html#cfn-wisdom-aiprompt-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def assistant_id(self) -> typing.Optional[builtins.str]:
        '''The identifier of the Amazon Q in Connect assistant.

        Can be either the ID or the ARN. URLs cannot contain the ARN.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiprompt.html#cfn-wisdom-aiprompt-assistantid
        '''
        result = self._values.get("assistant_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the AI Prompt.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiprompt.html#cfn-wisdom-aiprompt-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the AI Prompt.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiprompt.html#cfn-wisdom-aiprompt-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags used to organize, track, or control access for this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiprompt.html#cfn-wisdom-aiprompt-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAIPromptProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnAIPromptVersion(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_wisdom.CfnAIPromptVersion",
):
    '''Creates an Amazon Q in Connect AI Prompt version.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aipromptversion.html
    :cloudformationResource: AWS::Wisdom::AIPromptVersion
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_wisdom as wisdom
        
        cfn_aIPrompt_version = wisdom.CfnAIPromptVersion(self, "MyCfnAIPromptVersion",
            ai_prompt_id="aiPromptId",
            assistant_id="assistantId",
        
            # the properties below are optional
            modified_time_seconds=123
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        ai_prompt_id: builtins.str,
        assistant_id: builtins.str,
        modified_time_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param ai_prompt_id: The identifier of the Amazon Q in Connect AI prompt.
        :param assistant_id: The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
        :param modified_time_seconds: The time the AI Prompt version was last modified in seconds.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__729db38c828e5e73ae0386aea45298b479e1a069777600fadadd338035a13e5d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAIPromptVersionProps(
            ai_prompt_id=ai_prompt_id,
            assistant_id=assistant_id,
            modified_time_seconds=modified_time_seconds,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb551060d0407b951291352d04af15e21651dd34a52774e39a2d2da6e4df3220)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b234db791908c37519c8ae3284494dc43affe3bad0ab4eadab6407ef7ccc7627)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAiPromptArn")
    def attr_ai_prompt_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: AIPromptArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAiPromptArn"))

    @builtins.property
    @jsii.member(jsii_name="attrAiPromptVersionId")
    def attr_ai_prompt_version_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: AIPromptVersionId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAiPromptVersionId"))

    @builtins.property
    @jsii.member(jsii_name="attrAssistantArn")
    def attr_assistant_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: AssistantArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAssistantArn"))

    @builtins.property
    @jsii.member(jsii_name="attrVersionNumber")
    def attr_version_number(self) -> _IResolvable_da3f097b:
        '''The version number for this AI Prompt version.

        :cloudformationAttribute: VersionNumber
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrVersionNumber"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="aiPromptId")
    def ai_prompt_id(self) -> builtins.str:
        '''The identifier of the Amazon Q in Connect AI prompt.'''
        return typing.cast(builtins.str, jsii.get(self, "aiPromptId"))

    @ai_prompt_id.setter
    def ai_prompt_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad29e2ee6fad75de44645890c2c623b9ccb35a02f6e75d7ed98fa3b7337272ca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aiPromptId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="assistantId")
    def assistant_id(self) -> builtins.str:
        '''The identifier of the Amazon Q in Connect assistant.'''
        return typing.cast(builtins.str, jsii.get(self, "assistantId"))

    @assistant_id.setter
    def assistant_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b6982f0f13d49bf234e47082e4a9783bc461e6dc18d68737a370a3682f93b48)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assistantId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="modifiedTimeSeconds")
    def modified_time_seconds(self) -> typing.Optional[jsii.Number]:
        '''The time the AI Prompt version was last modified in seconds.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "modifiedTimeSeconds"))

    @modified_time_seconds.setter
    def modified_time_seconds(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1f64ffa51639af07e9712d95780a238db8bd368a440a159ead5f0364951dcd4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "modifiedTimeSeconds", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_wisdom.CfnAIPromptVersionProps",
    jsii_struct_bases=[],
    name_mapping={
        "ai_prompt_id": "aiPromptId",
        "assistant_id": "assistantId",
        "modified_time_seconds": "modifiedTimeSeconds",
    },
)
class CfnAIPromptVersionProps:
    def __init__(
        self,
        *,
        ai_prompt_id: builtins.str,
        assistant_id: builtins.str,
        modified_time_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Properties for defining a ``CfnAIPromptVersion``.

        :param ai_prompt_id: The identifier of the Amazon Q in Connect AI prompt.
        :param assistant_id: The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
        :param modified_time_seconds: The time the AI Prompt version was last modified in seconds.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aipromptversion.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_wisdom as wisdom
            
            cfn_aIPrompt_version_props = wisdom.CfnAIPromptVersionProps(
                ai_prompt_id="aiPromptId",
                assistant_id="assistantId",
            
                # the properties below are optional
                modified_time_seconds=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39068faf047cdd2f1dce0d86adaff6f71058bba08c161da563b36647959f2add)
            check_type(argname="argument ai_prompt_id", value=ai_prompt_id, expected_type=type_hints["ai_prompt_id"])
            check_type(argname="argument assistant_id", value=assistant_id, expected_type=type_hints["assistant_id"])
            check_type(argname="argument modified_time_seconds", value=modified_time_seconds, expected_type=type_hints["modified_time_seconds"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ai_prompt_id": ai_prompt_id,
            "assistant_id": assistant_id,
        }
        if modified_time_seconds is not None:
            self._values["modified_time_seconds"] = modified_time_seconds

    @builtins.property
    def ai_prompt_id(self) -> builtins.str:
        '''The identifier of the Amazon Q in Connect AI prompt.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aipromptversion.html#cfn-wisdom-aipromptversion-aipromptid
        '''
        result = self._values.get("ai_prompt_id")
        assert result is not None, "Required property 'ai_prompt_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def assistant_id(self) -> builtins.str:
        '''The identifier of the Amazon Q in Connect assistant.

        Can be either the ID or the ARN. URLs cannot contain the ARN.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aipromptversion.html#cfn-wisdom-aipromptversion-assistantid
        '''
        result = self._values.get("assistant_id")
        assert result is not None, "Required property 'assistant_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def modified_time_seconds(self) -> typing.Optional[jsii.Number]:
        '''The time the AI Prompt version was last modified in seconds.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aipromptversion.html#cfn-wisdom-aipromptversion-modifiedtimeseconds
        '''
        result = self._values.get("modified_time_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAIPromptVersionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnAssistant(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_wisdom.CfnAssistant",
):
    '''Specifies an Amazon Connect Wisdom assistant.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistant.html
    :cloudformationResource: AWS::Wisdom::Assistant
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_wisdom as wisdom
        
        cfn_assistant = wisdom.CfnAssistant(self, "MyCfnAssistant",
            name="name",
            type="type",
        
            # the properties below are optional
            description="description",
            server_side_encryption_configuration=wisdom.CfnAssistant.ServerSideEncryptionConfigurationProperty(
                kms_key_id="kmsKeyId"
            ),
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        server_side_encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAssistant.ServerSideEncryptionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the assistant.
        :param type: The type of assistant.
        :param description: The description of the assistant.
        :param server_side_encryption_configuration: The configuration information for the customer managed key used for encryption. The customer managed key must have a policy that allows ``kms:CreateGrant`` and ``kms:DescribeKey`` permissions to the IAM identity using the key to invoke Wisdom. To use Wisdom with chat, the key policy must also allow ``kms:Decrypt`` , ``kms:GenerateDataKey*`` , and ``kms:DescribeKey`` permissions to the ``connect.amazonaws.com`` service principal. For more information about setting up a customer managed key for Wisdom, see `Enable Amazon Connect Wisdom for your instance <https://docs.aws.amazon.com/connect/latest/adminguide/enable-wisdom.html>`_ .
        :param tags: The tags used to organize, track, or control access for this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8078b7e28a17a68ab6f3d362e7de3af6b6867207690b2b344e35797cd6569746)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAssistantProps(
            name=name,
            type=type,
            description=description,
            server_side_encryption_configuration=server_side_encryption_configuration,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67a0860b53a1867e3124a155db57aa1ab8bbb2d50c48a1553f8766101996d0b8)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a17095196842a083c7a71c961443f89f6d1dd766154e06248d10cdee66b0113)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAssistantArn")
    def attr_assistant_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the assistant.

        :cloudformationAttribute: AssistantArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAssistantArn"))

    @builtins.property
    @jsii.member(jsii_name="attrAssistantId")
    def attr_assistant_id(self) -> builtins.str:
        '''The ID of the Wisdom assistant.

        :cloudformationAttribute: AssistantId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAssistantId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the assistant.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ded25c09bd072cbcb02cdfdf40580d154663664980378f96c5210edc137dd8c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''The type of assistant.'''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c131b16ef6a21690f65d4e643bc0f04ea3e1fa9afd2bbf0e89a9bd4b96032657)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the assistant.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17115c2ceb35036c54e25dfa13fd4465303e5a759aae943761c84163427b74ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="serverSideEncryptionConfiguration")
    def server_side_encryption_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAssistant.ServerSideEncryptionConfigurationProperty"]]:
        '''The configuration information for the customer managed key used for encryption.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAssistant.ServerSideEncryptionConfigurationProperty"]], jsii.get(self, "serverSideEncryptionConfiguration"))

    @server_side_encryption_configuration.setter
    def server_side_encryption_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAssistant.ServerSideEncryptionConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb8470e364668ea9060baa4a3306507e0ded02773f75cc435d33474d30577d1b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverSideEncryptionConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a82c89946835215b7304a7033eacc23c202ee6ae8e17e73d0ba34f1dbaf1416)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnAssistant.ServerSideEncryptionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"kms_key_id": "kmsKeyId"},
    )
    class ServerSideEncryptionConfigurationProperty:
        def __init__(self, *, kms_key_id: typing.Optional[builtins.str] = None) -> None:
            '''The configuration information for the customer managed key used for encryption.

            :param kms_key_id: The customer managed key used for encryption. The customer managed key must have a policy that allows ``kms:CreateGrant`` and ``kms:DescribeKey`` permissions to the IAM identity using the key to invoke Wisdom. To use Wisdom with chat, the key policy must also allow ``kms:Decrypt`` , ``kms:GenerateDataKey*`` , and ``kms:DescribeKey`` permissions to the ``connect.amazonaws.com`` service principal. For more information about setting up a customer managed key for Wisdom, see `Enable Amazon Connect Wisdom for your instance <https://docs.aws.amazon.com/connect/latest/adminguide/enable-wisdom.html>`_ . For information about valid ID values, see `Key identifiers (KeyId) <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id>`_ in the *AWS Key Management Service Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-assistant-serversideencryptionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                server_side_encryption_configuration_property = wisdom.CfnAssistant.ServerSideEncryptionConfigurationProperty(
                    kms_key_id="kmsKeyId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fa78e1cc313485ba353b8f1dc8b01c69bcdd1c5bcecd204b9778596de1e4a07d)
                check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if kms_key_id is not None:
                self._values["kms_key_id"] = kms_key_id

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            '''The customer managed key used for encryption.

            The customer managed key must have a policy that allows ``kms:CreateGrant`` and ``kms:DescribeKey`` permissions to the IAM identity using the key to invoke Wisdom. To use Wisdom with chat, the key policy must also allow ``kms:Decrypt`` , ``kms:GenerateDataKey*`` , and ``kms:DescribeKey`` permissions to the ``connect.amazonaws.com`` service principal. For more information about setting up a customer managed key for Wisdom, see `Enable Amazon Connect Wisdom for your instance <https://docs.aws.amazon.com/connect/latest/adminguide/enable-wisdom.html>`_ . For information about valid ID values, see `Key identifiers (KeyId) <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id>`_ in the *AWS Key Management Service Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-assistant-serversideencryptionconfiguration.html#cfn-wisdom-assistant-serversideencryptionconfiguration-kmskeyid
            '''
            result = self._values.get("kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ServerSideEncryptionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnAssistantAssociation(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_wisdom.CfnAssistantAssociation",
):
    '''Specifies an association between an Amazon Connect Wisdom assistant and another resource.

    Currently, the only supported association is with a knowledge base. An assistant can have only a single association.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistantassociation.html
    :cloudformationResource: AWS::Wisdom::AssistantAssociation
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_wisdom as wisdom
        
        cfn_assistant_association = wisdom.CfnAssistantAssociation(self, "MyCfnAssistantAssociation",
            assistant_id="assistantId",
            association=wisdom.CfnAssistantAssociation.AssociationDataProperty(
                knowledge_base_id="knowledgeBaseId"
            ),
            association_type="associationType",
        
            # the properties below are optional
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        assistant_id: builtins.str,
        association: typing.Union[_IResolvable_da3f097b, typing.Union["CfnAssistantAssociation.AssociationDataProperty", typing.Dict[builtins.str, typing.Any]]],
        association_type: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param assistant_id: The identifier of the Wisdom assistant.
        :param association: The identifier of the associated resource.
        :param association_type: The type of association.
        :param tags: The tags used to organize, track, or control access for this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17f6f8491bb7be7dab63c57bf64b65f643c4fece381b02f49002f796c7a8f0f9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAssistantAssociationProps(
            assistant_id=assistant_id,
            association=association,
            association_type=association_type,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a96af34ce4ed10cd5d626bf5df7799b86ca3023d4f6b302c0cdb51a0bdd1274)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e84fe37792368fc9821204b49ed0d6e13642f35bcdc7bb2676de0ee949767075)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAssistantArn")
    def attr_assistant_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the Wisdom assistant.

        :cloudformationAttribute: AssistantArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAssistantArn"))

    @builtins.property
    @jsii.member(jsii_name="attrAssistantAssociationArn")
    def attr_assistant_association_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the assistant association.

        :cloudformationAttribute: AssistantAssociationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAssistantAssociationArn"))

    @builtins.property
    @jsii.member(jsii_name="attrAssistantAssociationId")
    def attr_assistant_association_id(self) -> builtins.str:
        '''The ID of the association.

        :cloudformationAttribute: AssistantAssociationId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAssistantAssociationId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="assistantId")
    def assistant_id(self) -> builtins.str:
        '''The identifier of the Wisdom assistant.'''
        return typing.cast(builtins.str, jsii.get(self, "assistantId"))

    @assistant_id.setter
    def assistant_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c72c215a467df1527e01f95d41dc85287728a80fa94729b3ff14b2b1312fb30)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assistantId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="association")
    def association(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnAssistantAssociation.AssociationDataProperty"]:
        '''The identifier of the associated resource.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnAssistantAssociation.AssociationDataProperty"], jsii.get(self, "association"))

    @association.setter
    def association(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnAssistantAssociation.AssociationDataProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e46eeb6364ccf0b8f92618927437f56df6248417cb401c056b83fe5692feb0f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "association", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="associationType")
    def association_type(self) -> builtins.str:
        '''The type of association.'''
        return typing.cast(builtins.str, jsii.get(self, "associationType"))

    @association_type.setter
    def association_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48fcb269f8dde8b147d1a0d7681e40817cb35b599f00a24aff263a84df4cea90)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "associationType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea3d3cb4fe1048c256fc8719ac3d18f47cb21ef29730dd9d1f53a9304ccd4030)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnAssistantAssociation.AssociationDataProperty",
        jsii_struct_bases=[],
        name_mapping={"knowledge_base_id": "knowledgeBaseId"},
    )
    class AssociationDataProperty:
        def __init__(self, *, knowledge_base_id: builtins.str) -> None:
            '''A union type that currently has a single argument, which is the knowledge base ID.

            :param knowledge_base_id: The identifier of the knowledge base.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-assistantassociation-associationdata.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                association_data_property = wisdom.CfnAssistantAssociation.AssociationDataProperty(
                    knowledge_base_id="knowledgeBaseId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f6ecf0cfb2eb97624a8ec4ab51e16f75cfa1a5397890274252a2621ff5ad378d)
                check_type(argname="argument knowledge_base_id", value=knowledge_base_id, expected_type=type_hints["knowledge_base_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "knowledge_base_id": knowledge_base_id,
            }

        @builtins.property
        def knowledge_base_id(self) -> builtins.str:
            '''The identifier of the knowledge base.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-assistantassociation-associationdata.html#cfn-wisdom-assistantassociation-associationdata-knowledgebaseid
            '''
            result = self._values.get("knowledge_base_id")
            assert result is not None, "Required property 'knowledge_base_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AssociationDataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_wisdom.CfnAssistantAssociationProps",
    jsii_struct_bases=[],
    name_mapping={
        "assistant_id": "assistantId",
        "association": "association",
        "association_type": "associationType",
        "tags": "tags",
    },
)
class CfnAssistantAssociationProps:
    def __init__(
        self,
        *,
        assistant_id: builtins.str,
        association: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssistantAssociation.AssociationDataProperty, typing.Dict[builtins.str, typing.Any]]],
        association_type: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnAssistantAssociation``.

        :param assistant_id: The identifier of the Wisdom assistant.
        :param association: The identifier of the associated resource.
        :param association_type: The type of association.
        :param tags: The tags used to organize, track, or control access for this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistantassociation.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_wisdom as wisdom
            
            cfn_assistant_association_props = wisdom.CfnAssistantAssociationProps(
                assistant_id="assistantId",
                association=wisdom.CfnAssistantAssociation.AssociationDataProperty(
                    knowledge_base_id="knowledgeBaseId"
                ),
                association_type="associationType",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__419e70156a249f4fa2bea77a71d532fe9a351e3d150b5939dc8455b174375514)
            check_type(argname="argument assistant_id", value=assistant_id, expected_type=type_hints["assistant_id"])
            check_type(argname="argument association", value=association, expected_type=type_hints["association"])
            check_type(argname="argument association_type", value=association_type, expected_type=type_hints["association_type"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "assistant_id": assistant_id,
            "association": association,
            "association_type": association_type,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def assistant_id(self) -> builtins.str:
        '''The identifier of the Wisdom assistant.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistantassociation.html#cfn-wisdom-assistantassociation-assistantid
        '''
        result = self._values.get("assistant_id")
        assert result is not None, "Required property 'assistant_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def association(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnAssistantAssociation.AssociationDataProperty]:
        '''The identifier of the associated resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistantassociation.html#cfn-wisdom-assistantassociation-association
        '''
        result = self._values.get("association")
        assert result is not None, "Required property 'association' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnAssistantAssociation.AssociationDataProperty], result)

    @builtins.property
    def association_type(self) -> builtins.str:
        '''The type of association.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistantassociation.html#cfn-wisdom-assistantassociation-associationtype
        '''
        result = self._values.get("association_type")
        assert result is not None, "Required property 'association_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistantassociation.html#cfn-wisdom-assistantassociation-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAssistantAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_wisdom.CfnAssistantProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "type": "type",
        "description": "description",
        "server_side_encryption_configuration": "serverSideEncryptionConfiguration",
        "tags": "tags",
    },
)
class CfnAssistantProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        server_side_encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssistant.ServerSideEncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnAssistant``.

        :param name: The name of the assistant.
        :param type: The type of assistant.
        :param description: The description of the assistant.
        :param server_side_encryption_configuration: The configuration information for the customer managed key used for encryption. The customer managed key must have a policy that allows ``kms:CreateGrant`` and ``kms:DescribeKey`` permissions to the IAM identity using the key to invoke Wisdom. To use Wisdom with chat, the key policy must also allow ``kms:Decrypt`` , ``kms:GenerateDataKey*`` , and ``kms:DescribeKey`` permissions to the ``connect.amazonaws.com`` service principal. For more information about setting up a customer managed key for Wisdom, see `Enable Amazon Connect Wisdom for your instance <https://docs.aws.amazon.com/connect/latest/adminguide/enable-wisdom.html>`_ .
        :param tags: The tags used to organize, track, or control access for this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistant.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_wisdom as wisdom
            
            cfn_assistant_props = wisdom.CfnAssistantProps(
                name="name",
                type="type",
            
                # the properties below are optional
                description="description",
                server_side_encryption_configuration=wisdom.CfnAssistant.ServerSideEncryptionConfigurationProperty(
                    kms_key_id="kmsKeyId"
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2f6978729a0bccb7cc077df26ee5d379812791b9fe7ec0622251ed958562e07)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument server_side_encryption_configuration", value=server_side_encryption_configuration, expected_type=type_hints["server_side_encryption_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "type": type,
        }
        if description is not None:
            self._values["description"] = description
        if server_side_encryption_configuration is not None:
            self._values["server_side_encryption_configuration"] = server_side_encryption_configuration
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the assistant.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistant.html#cfn-wisdom-assistant-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of assistant.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistant.html#cfn-wisdom-assistant-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the assistant.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistant.html#cfn-wisdom-assistant-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def server_side_encryption_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAssistant.ServerSideEncryptionConfigurationProperty]]:
        '''The configuration information for the customer managed key used for encryption.

        The customer managed key must have a policy that allows ``kms:CreateGrant`` and ``kms:DescribeKey`` permissions to the IAM identity using the key to invoke Wisdom. To use Wisdom with chat, the key policy must also allow ``kms:Decrypt`` , ``kms:GenerateDataKey*`` , and ``kms:DescribeKey`` permissions to the ``connect.amazonaws.com`` service principal. For more information about setting up a customer managed key for Wisdom, see `Enable Amazon Connect Wisdom for your instance <https://docs.aws.amazon.com/connect/latest/adminguide/enable-wisdom.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistant.html#cfn-wisdom-assistant-serversideencryptionconfiguration
        '''
        result = self._values.get("server_side_encryption_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAssistant.ServerSideEncryptionConfigurationProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistant.html#cfn-wisdom-assistant-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAssistantProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnKnowledgeBase(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_wisdom.CfnKnowledgeBase",
):
    '''Specifies a knowledge base.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-knowledgebase.html
    :cloudformationResource: AWS::Wisdom::KnowledgeBase
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_wisdom as wisdom
        
        cfn_knowledge_base = wisdom.CfnKnowledgeBase(self, "MyCfnKnowledgeBase",
            knowledge_base_type="knowledgeBaseType",
            name="name",
        
            # the properties below are optional
            description="description",
            rendering_configuration=wisdom.CfnKnowledgeBase.RenderingConfigurationProperty(
                template_uri="templateUri"
            ),
            server_side_encryption_configuration=wisdom.CfnKnowledgeBase.ServerSideEncryptionConfigurationProperty(
                kms_key_id="kmsKeyId"
            ),
            source_configuration=wisdom.CfnKnowledgeBase.SourceConfigurationProperty(
                app_integrations=wisdom.CfnKnowledgeBase.AppIntegrationsConfigurationProperty(
                    app_integration_arn="appIntegrationArn",
        
                    # the properties below are optional
                    object_fields=["objectFields"]
                )
            ),
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        knowledge_base_type: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        rendering_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnKnowledgeBase.RenderingConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        server_side_encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnKnowledgeBase.ServerSideEncryptionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        source_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnKnowledgeBase.SourceConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param knowledge_base_type: The type of knowledge base. Only CUSTOM knowledge bases allow you to upload your own content. EXTERNAL knowledge bases support integrations with third-party systems whose content is synchronized automatically.
        :param name: The name of the knowledge base.
        :param description: The description.
        :param rendering_configuration: Information about how to render the content.
        :param server_side_encryption_configuration: This customer managed key must have a policy that allows ``kms:CreateGrant`` and ``kms:DescribeKey`` permissions to the IAM identity using the key to invoke Wisdom. For more information about setting up a customer managed key for Wisdom, see `Enable Amazon Connect Wisdom for your instance <https://docs.aws.amazon.com/connect/latest/adminguide/enable-wisdom.html>`_ . For information about valid ID values, see `Key identifiers (KeyId) <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id>`_ in the *AWS Key Management Service Developer Guide* .
        :param source_configuration: The source of the knowledge base content. Only set this argument for EXTERNAL or Managed knowledge bases.
        :param tags: The tags used to organize, track, or control access for this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99512a2eb8a3e47802b889aac668fc94bdc0534ee683313dac712b20006ea6ed)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnKnowledgeBaseProps(
            knowledge_base_type=knowledge_base_type,
            name=name,
            description=description,
            rendering_configuration=rendering_configuration,
            server_side_encryption_configuration=server_side_encryption_configuration,
            source_configuration=source_configuration,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e12fde615d3c7854b4e97326fea29e89d837485efe274039378606ee08a4be76)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__198b767f5d7e7dce9b330a5c5c43441fed236182c59b06b0be2da034b14ce256)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrKnowledgeBaseArn")
    def attr_knowledge_base_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the knowledge base.

        :cloudformationAttribute: KnowledgeBaseArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrKnowledgeBaseArn"))

    @builtins.property
    @jsii.member(jsii_name="attrKnowledgeBaseId")
    def attr_knowledge_base_id(self) -> builtins.str:
        '''The ID of the knowledge base.

        :cloudformationAttribute: KnowledgeBaseId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrKnowledgeBaseId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="knowledgeBaseType")
    def knowledge_base_type(self) -> builtins.str:
        '''The type of knowledge base.'''
        return typing.cast(builtins.str, jsii.get(self, "knowledgeBaseType"))

    @knowledge_base_type.setter
    def knowledge_base_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93bc0b75027c2aaed7afea32df7bbe9ea25daf054d032e869d4b65d3c73427e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "knowledgeBaseType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the knowledge base.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06da4251d33a92a96fd91655710caf394cf4fa6fe728e86b20be47c80f50c450)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8e87e39918fdfb349935e6c5b5b76307ecd838c21583fab217f7d88ca3ea67c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="renderingConfiguration")
    def rendering_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.RenderingConfigurationProperty"]]:
        '''Information about how to render the content.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.RenderingConfigurationProperty"]], jsii.get(self, "renderingConfiguration"))

    @rendering_configuration.setter
    def rendering_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.RenderingConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3dbfe6a279891a574d7128da28db41ca74ec109e76fb61b5b9db27b1ee815fba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "renderingConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="serverSideEncryptionConfiguration")
    def server_side_encryption_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.ServerSideEncryptionConfigurationProperty"]]:
        '''This customer managed key must have a policy that allows ``kms:CreateGrant`` and ``kms:DescribeKey`` permissions to the IAM identity using the key to invoke Wisdom.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.ServerSideEncryptionConfigurationProperty"]], jsii.get(self, "serverSideEncryptionConfiguration"))

    @server_side_encryption_configuration.setter
    def server_side_encryption_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.ServerSideEncryptionConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__221e4b62cf601d8c0e6300aceb9f7a7bfe38ac19093345137be6abb3f22756d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverSideEncryptionConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sourceConfiguration")
    def source_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.SourceConfigurationProperty"]]:
        '''The source of the knowledge base content.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.SourceConfigurationProperty"]], jsii.get(self, "sourceConfiguration"))

    @source_configuration.setter
    def source_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.SourceConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ab7292e64b294c529dec00a33cfb2da96ff80581b3e1376c67027a944849691)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b654968450798e9434ae157e80b0efdde965d3d9cf517c41c4fcdcfa66e910f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnKnowledgeBase.AppIntegrationsConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "app_integration_arn": "appIntegrationArn",
            "object_fields": "objectFields",
        },
    )
    class AppIntegrationsConfigurationProperty:
        def __init__(
            self,
            *,
            app_integration_arn: builtins.str,
            object_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Configuration information for Amazon AppIntegrations to automatically ingest content.

            :param app_integration_arn: The Amazon Resource Name (ARN) of the AppIntegrations DataIntegration to use for ingesting content. - For `Salesforce <https://docs.aws.amazon.com/https://developer.salesforce.com/docs/atlas.en-us.knowledge_dev.meta/knowledge_dev/sforce_api_objects_knowledge__kav.htm>`_ , your AppIntegrations DataIntegration must have an ObjectConfiguration if objectFields is not provided, including at least ``Id`` , ``ArticleNumber`` , ``VersionNumber`` , ``Title`` , ``PublishStatus`` , and ``IsDeleted`` as source fields. - For `ServiceNow <https://docs.aws.amazon.com/https://developer.servicenow.com/dev.do#!/reference/api/rome/rest/knowledge-management-api>`_ , your AppIntegrations DataIntegration must have an ObjectConfiguration if objectFields is not provided, including at least ``number`` , ``short_description`` , ``sys_mod_count`` , ``workflow_state`` , and ``active`` as source fields. - For `Zendesk <https://docs.aws.amazon.com/https://developer.zendesk.com/api-reference/help_center/help-center-api/articles/>`_ , your AppIntegrations DataIntegration must have an ObjectConfiguration if ``objectFields`` is not provided, including at least ``id`` , ``title`` , ``updated_at`` , and ``draft`` as source fields. - For `SharePoint <https://docs.aws.amazon.com/https://learn.microsoft.com/en-us/sharepoint/dev/sp-add-ins/sharepoint-net-server-csom-jsom-and-rest-api-index>`_ , your AppIntegrations DataIntegration must have a FileConfiguration, including only file extensions that are among ``docx`` , ``pdf`` , ``html`` , ``htm`` , and ``txt`` . - For `Amazon S3 <https://docs.aws.amazon.com/s3/>`_ , the ObjectConfiguration and FileConfiguration of your AppIntegrations DataIntegration must be null. The ``SourceURI`` of your DataIntegration must use the following format: ``s3://your_s3_bucket_name`` . .. epigraph:: The bucket policy of the corresponding S3 bucket must allow the AWS principal ``app-integrations.amazonaws.com`` to perform ``s3:ListBucket`` , ``s3:GetObject`` , and ``s3:GetBucketLocation`` against the bucket.
            :param object_fields: The fields from the source that are made available to your agents in Amazon Q in Connect. Optional if ObjectConfiguration is included in the provided DataIntegration. - For `Salesforce <https://docs.aws.amazon.com/https://developer.salesforce.com/docs/atlas.en-us.knowledge_dev.meta/knowledge_dev/sforce_api_objects_knowledge__kav.htm>`_ , you must include at least ``Id`` , ``ArticleNumber`` , ``VersionNumber`` , ``Title`` , ``PublishStatus`` , and ``IsDeleted`` . - For `ServiceNow <https://docs.aws.amazon.com/https://developer.servicenow.com/dev.do#!/reference/api/rome/rest/knowledge-management-api>`_ , you must include at least ``number`` , ``short_description`` , ``sys_mod_count`` , ``workflow_state`` , and ``active`` . - For `Zendesk <https://docs.aws.amazon.com/https://developer.zendesk.com/api-reference/help_center/help-center-api/articles/>`_ , you must include at least ``id`` , ``title`` , ``updated_at`` , and ``draft`` . Make sure to include additional fields. These fields are indexed and used to source recommendations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-appintegrationsconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                app_integrations_configuration_property = wisdom.CfnKnowledgeBase.AppIntegrationsConfigurationProperty(
                    app_integration_arn="appIntegrationArn",
                
                    # the properties below are optional
                    object_fields=["objectFields"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fb5af4edc537ecd6b5dab081c90708156852ccef10f7a6228ff445f6dc0e509c)
                check_type(argname="argument app_integration_arn", value=app_integration_arn, expected_type=type_hints["app_integration_arn"])
                check_type(argname="argument object_fields", value=object_fields, expected_type=type_hints["object_fields"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "app_integration_arn": app_integration_arn,
            }
            if object_fields is not None:
                self._values["object_fields"] = object_fields

        @builtins.property
        def app_integration_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the AppIntegrations DataIntegration to use for ingesting content.

            - For `Salesforce <https://docs.aws.amazon.com/https://developer.salesforce.com/docs/atlas.en-us.knowledge_dev.meta/knowledge_dev/sforce_api_objects_knowledge__kav.htm>`_ , your AppIntegrations DataIntegration must have an ObjectConfiguration if objectFields is not provided, including at least ``Id`` , ``ArticleNumber`` , ``VersionNumber`` , ``Title`` , ``PublishStatus`` , and ``IsDeleted`` as source fields.
            - For `ServiceNow <https://docs.aws.amazon.com/https://developer.servicenow.com/dev.do#!/reference/api/rome/rest/knowledge-management-api>`_ , your AppIntegrations DataIntegration must have an ObjectConfiguration if objectFields is not provided, including at least ``number`` , ``short_description`` , ``sys_mod_count`` , ``workflow_state`` , and ``active`` as source fields.
            - For `Zendesk <https://docs.aws.amazon.com/https://developer.zendesk.com/api-reference/help_center/help-center-api/articles/>`_ , your AppIntegrations DataIntegration must have an ObjectConfiguration if ``objectFields`` is not provided, including at least ``id`` , ``title`` , ``updated_at`` , and ``draft`` as source fields.
            - For `SharePoint <https://docs.aws.amazon.com/https://learn.microsoft.com/en-us/sharepoint/dev/sp-add-ins/sharepoint-net-server-csom-jsom-and-rest-api-index>`_ , your AppIntegrations DataIntegration must have a FileConfiguration, including only file extensions that are among ``docx`` , ``pdf`` , ``html`` , ``htm`` , and ``txt`` .
            - For `Amazon S3 <https://docs.aws.amazon.com/s3/>`_ , the ObjectConfiguration and FileConfiguration of your AppIntegrations DataIntegration must be null. The ``SourceURI`` of your DataIntegration must use the following format: ``s3://your_s3_bucket_name`` .

            .. epigraph::

               The bucket policy of the corresponding S3 bucket must allow the AWS principal ``app-integrations.amazonaws.com`` to perform ``s3:ListBucket`` , ``s3:GetObject`` , and ``s3:GetBucketLocation`` against the bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-appintegrationsconfiguration.html#cfn-wisdom-knowledgebase-appintegrationsconfiguration-appintegrationarn
            '''
            result = self._values.get("app_integration_arn")
            assert result is not None, "Required property 'app_integration_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def object_fields(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The fields from the source that are made available to your agents in Amazon Q in Connect.

            Optional if ObjectConfiguration is included in the provided DataIntegration.

            - For `Salesforce <https://docs.aws.amazon.com/https://developer.salesforce.com/docs/atlas.en-us.knowledge_dev.meta/knowledge_dev/sforce_api_objects_knowledge__kav.htm>`_ , you must include at least ``Id`` , ``ArticleNumber`` , ``VersionNumber`` , ``Title`` , ``PublishStatus`` , and ``IsDeleted`` .
            - For `ServiceNow <https://docs.aws.amazon.com/https://developer.servicenow.com/dev.do#!/reference/api/rome/rest/knowledge-management-api>`_ , you must include at least ``number`` , ``short_description`` , ``sys_mod_count`` , ``workflow_state`` , and ``active`` .
            - For `Zendesk <https://docs.aws.amazon.com/https://developer.zendesk.com/api-reference/help_center/help-center-api/articles/>`_ , you must include at least ``id`` , ``title`` , ``updated_at`` , and ``draft`` .

            Make sure to include additional fields. These fields are indexed and used to source recommendations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-appintegrationsconfiguration.html#cfn-wisdom-knowledgebase-appintegrationsconfiguration-objectfields
            '''
            result = self._values.get("object_fields")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AppIntegrationsConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnKnowledgeBase.RenderingConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"template_uri": "templateUri"},
    )
    class RenderingConfigurationProperty:
        def __init__(
            self,
            *,
            template_uri: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Information about how to render the content.

            :param template_uri: A URI template containing exactly one variable in ``${variableName}`` format. This can only be set for ``EXTERNAL`` knowledge bases. For Salesforce, ServiceNow, and Zendesk, the variable must be one of the following: - Salesforce: ``Id`` , ``ArticleNumber`` , ``VersionNumber`` , ``Title`` , ``PublishStatus`` , or ``IsDeleted`` - ServiceNow: ``number`` , ``short_description`` , ``sys_mod_count`` , ``workflow_state`` , or ``active`` - Zendesk: ``id`` , ``title`` , ``updated_at`` , or ``draft`` The variable is replaced with the actual value for a piece of content when calling `GetContent <https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_GetContent.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-renderingconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                rendering_configuration_property = wisdom.CfnKnowledgeBase.RenderingConfigurationProperty(
                    template_uri="templateUri"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bc0b3350c030b63153dd14a7ab6b7c686549027289e97b41678c46c5c9bce0d1)
                check_type(argname="argument template_uri", value=template_uri, expected_type=type_hints["template_uri"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if template_uri is not None:
                self._values["template_uri"] = template_uri

        @builtins.property
        def template_uri(self) -> typing.Optional[builtins.str]:
            '''A URI template containing exactly one variable in ``${variableName}`` format.

            This can only be set for ``EXTERNAL`` knowledge bases. For Salesforce, ServiceNow, and Zendesk, the variable must be one of the following:

            - Salesforce: ``Id`` , ``ArticleNumber`` , ``VersionNumber`` , ``Title`` , ``PublishStatus`` , or ``IsDeleted``
            - ServiceNow: ``number`` , ``short_description`` , ``sys_mod_count`` , ``workflow_state`` , or ``active``
            - Zendesk: ``id`` , ``title`` , ``updated_at`` , or ``draft``

            The variable is replaced with the actual value for a piece of content when calling `GetContent <https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_GetContent.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-renderingconfiguration.html#cfn-wisdom-knowledgebase-renderingconfiguration-templateuri
            '''
            result = self._values.get("template_uri")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RenderingConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnKnowledgeBase.ServerSideEncryptionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"kms_key_id": "kmsKeyId"},
    )
    class ServerSideEncryptionConfigurationProperty:
        def __init__(self, *, kms_key_id: typing.Optional[builtins.str] = None) -> None:
            '''The configuration information for the customer managed key used for encryption.

            :param kms_key_id: The customer managed key used for encryption. This customer managed key must have a policy that allows ``kms:CreateGrant`` and ``kms:DescribeKey`` permissions to the IAM identity using the key to invoke Wisdom. For more information about setting up a customer managed key for Wisdom, see `Enable Amazon Connect Wisdom for your instance <https://docs.aws.amazon.com/connect/latest/adminguide/enable-wisdom.html>`_ . For information about valid ID values, see `Key identifiers (KeyId) <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-serversideencryptionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                server_side_encryption_configuration_property = wisdom.CfnKnowledgeBase.ServerSideEncryptionConfigurationProperty(
                    kms_key_id="kmsKeyId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f0cd7e6721b8c282e7e8effcea12ef5d59096c2d9eb9611a2269ac2deff0e697)
                check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if kms_key_id is not None:
                self._values["kms_key_id"] = kms_key_id

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            '''The customer managed key used for encryption.

            This customer managed key must have a policy that allows ``kms:CreateGrant`` and ``kms:DescribeKey`` permissions to the IAM identity using the key to invoke Wisdom.

            For more information about setting up a customer managed key for Wisdom, see `Enable Amazon Connect Wisdom for your instance <https://docs.aws.amazon.com/connect/latest/adminguide/enable-wisdom.html>`_ . For information about valid ID values, see `Key identifiers (KeyId) <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-serversideencryptionconfiguration.html#cfn-wisdom-knowledgebase-serversideencryptionconfiguration-kmskeyid
            '''
            result = self._values.get("kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ServerSideEncryptionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnKnowledgeBase.SourceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"app_integrations": "appIntegrations"},
    )
    class SourceConfigurationProperty:
        def __init__(
            self,
            *,
            app_integrations: typing.Union[_IResolvable_da3f097b, typing.Union["CfnKnowledgeBase.AppIntegrationsConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Configuration information about the external data source.

            :param app_integrations: Configuration information for Amazon AppIntegrations to automatically ingest content.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-sourceconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                source_configuration_property = wisdom.CfnKnowledgeBase.SourceConfigurationProperty(
                    app_integrations=wisdom.CfnKnowledgeBase.AppIntegrationsConfigurationProperty(
                        app_integration_arn="appIntegrationArn",
                
                        # the properties below are optional
                        object_fields=["objectFields"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__169c34939e73e3c8ce81d921898915b159d4e29ad0c3757e50950775728d0aa0)
                check_type(argname="argument app_integrations", value=app_integrations, expected_type=type_hints["app_integrations"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "app_integrations": app_integrations,
            }

        @builtins.property
        def app_integrations(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.AppIntegrationsConfigurationProperty"]:
            '''Configuration information for Amazon AppIntegrations to automatically ingest content.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-sourceconfiguration.html#cfn-wisdom-knowledgebase-sourceconfiguration-appintegrations
            '''
            result = self._values.get("app_integrations")
            assert result is not None, "Required property 'app_integrations' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.AppIntegrationsConfigurationProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_wisdom.CfnKnowledgeBaseProps",
    jsii_struct_bases=[],
    name_mapping={
        "knowledge_base_type": "knowledgeBaseType",
        "name": "name",
        "description": "description",
        "rendering_configuration": "renderingConfiguration",
        "server_side_encryption_configuration": "serverSideEncryptionConfiguration",
        "source_configuration": "sourceConfiguration",
        "tags": "tags",
    },
)
class CfnKnowledgeBaseProps:
    def __init__(
        self,
        *,
        knowledge_base_type: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        rendering_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnKnowledgeBase.RenderingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        server_side_encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnKnowledgeBase.ServerSideEncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        source_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnKnowledgeBase.SourceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnKnowledgeBase``.

        :param knowledge_base_type: The type of knowledge base. Only CUSTOM knowledge bases allow you to upload your own content. EXTERNAL knowledge bases support integrations with third-party systems whose content is synchronized automatically.
        :param name: The name of the knowledge base.
        :param description: The description.
        :param rendering_configuration: Information about how to render the content.
        :param server_side_encryption_configuration: This customer managed key must have a policy that allows ``kms:CreateGrant`` and ``kms:DescribeKey`` permissions to the IAM identity using the key to invoke Wisdom. For more information about setting up a customer managed key for Wisdom, see `Enable Amazon Connect Wisdom for your instance <https://docs.aws.amazon.com/connect/latest/adminguide/enable-wisdom.html>`_ . For information about valid ID values, see `Key identifiers (KeyId) <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id>`_ in the *AWS Key Management Service Developer Guide* .
        :param source_configuration: The source of the knowledge base content. Only set this argument for EXTERNAL or Managed knowledge bases.
        :param tags: The tags used to organize, track, or control access for this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-knowledgebase.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_wisdom as wisdom
            
            cfn_knowledge_base_props = wisdom.CfnKnowledgeBaseProps(
                knowledge_base_type="knowledgeBaseType",
                name="name",
            
                # the properties below are optional
                description="description",
                rendering_configuration=wisdom.CfnKnowledgeBase.RenderingConfigurationProperty(
                    template_uri="templateUri"
                ),
                server_side_encryption_configuration=wisdom.CfnKnowledgeBase.ServerSideEncryptionConfigurationProperty(
                    kms_key_id="kmsKeyId"
                ),
                source_configuration=wisdom.CfnKnowledgeBase.SourceConfigurationProperty(
                    app_integrations=wisdom.CfnKnowledgeBase.AppIntegrationsConfigurationProperty(
                        app_integration_arn="appIntegrationArn",
            
                        # the properties below are optional
                        object_fields=["objectFields"]
                    )
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b2c89f78d66a3c10ed4851c5bc420028f69cc91ddabbe2ac038dd7332ea1edd)
            check_type(argname="argument knowledge_base_type", value=knowledge_base_type, expected_type=type_hints["knowledge_base_type"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument rendering_configuration", value=rendering_configuration, expected_type=type_hints["rendering_configuration"])
            check_type(argname="argument server_side_encryption_configuration", value=server_side_encryption_configuration, expected_type=type_hints["server_side_encryption_configuration"])
            check_type(argname="argument source_configuration", value=source_configuration, expected_type=type_hints["source_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "knowledge_base_type": knowledge_base_type,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if rendering_configuration is not None:
            self._values["rendering_configuration"] = rendering_configuration
        if server_side_encryption_configuration is not None:
            self._values["server_side_encryption_configuration"] = server_side_encryption_configuration
        if source_configuration is not None:
            self._values["source_configuration"] = source_configuration
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def knowledge_base_type(self) -> builtins.str:
        '''The type of knowledge base.

        Only CUSTOM knowledge bases allow you to upload your own content. EXTERNAL knowledge bases support integrations with third-party systems whose content is synchronized automatically.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-knowledgebase.html#cfn-wisdom-knowledgebase-knowledgebasetype
        '''
        result = self._values.get("knowledge_base_type")
        assert result is not None, "Required property 'knowledge_base_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the knowledge base.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-knowledgebase.html#cfn-wisdom-knowledgebase-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-knowledgebase.html#cfn-wisdom-knowledgebase-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rendering_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnKnowledgeBase.RenderingConfigurationProperty]]:
        '''Information about how to render the content.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-knowledgebase.html#cfn-wisdom-knowledgebase-renderingconfiguration
        '''
        result = self._values.get("rendering_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnKnowledgeBase.RenderingConfigurationProperty]], result)

    @builtins.property
    def server_side_encryption_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnKnowledgeBase.ServerSideEncryptionConfigurationProperty]]:
        '''This customer managed key must have a policy that allows ``kms:CreateGrant`` and ``kms:DescribeKey`` permissions to the IAM identity using the key to invoke Wisdom.

        For more information about setting up a customer managed key for Wisdom, see `Enable Amazon Connect Wisdom for your instance <https://docs.aws.amazon.com/connect/latest/adminguide/enable-wisdom.html>`_ . For information about valid ID values, see `Key identifiers (KeyId) <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id>`_ in the *AWS Key Management Service Developer Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-knowledgebase.html#cfn-wisdom-knowledgebase-serversideencryptionconfiguration
        '''
        result = self._values.get("server_side_encryption_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnKnowledgeBase.ServerSideEncryptionConfigurationProperty]], result)

    @builtins.property
    def source_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnKnowledgeBase.SourceConfigurationProperty]]:
        '''The source of the knowledge base content.

        Only set this argument for EXTERNAL or Managed knowledge bases.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-knowledgebase.html#cfn-wisdom-knowledgebase-sourceconfiguration
        '''
        result = self._values.get("source_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnKnowledgeBase.SourceConfigurationProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-knowledgebase.html#cfn-wisdom-knowledgebase-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnKnowledgeBaseProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAIAgent",
    "CfnAIAgentProps",
    "CfnAIAgentVersion",
    "CfnAIAgentVersionProps",
    "CfnAIPrompt",
    "CfnAIPromptProps",
    "CfnAIPromptVersion",
    "CfnAIPromptVersionProps",
    "CfnAssistant",
    "CfnAssistantAssociation",
    "CfnAssistantAssociationProps",
    "CfnAssistantProps",
    "CfnKnowledgeBase",
    "CfnKnowledgeBaseProps",
]

publication.publish()

def _typecheckingstub__e4d43de9ccaeb31eba5b0b613ecac25531a87bb9137652388e6196070f4622ab(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    assistant_id: builtins.str,
    configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIAgent.AIAgentConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    type: builtins.str,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__daf9bd162ab4eaa6b11972bcaf8372498a47b4ad8cf111130cabfae3f675d2b4(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__569f9e85834b9b380045c7e9789b3ac0684022e3b37642b34e232ba9b451ade6(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3d8fd38839efd97edc463e08adcbeb6d1b964aa278b19d07017fb40c806bb19(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d07c289ddb2abe8b14c5f581386f3377fb7266b5b099c89c1b142b4bbd9d769(
    value: typing.Union[_IResolvable_da3f097b, CfnAIAgent.AIAgentConfigurationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b90fdd18e60e92e1589e2bf61b55c6cd7758b9da5e26d00525cb08a2ad13830(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6380f3badbada0c208691bd5242dfabe1122f10b446d77f1ae5ad0c9da456ae8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__982490f39ff188d23898421a1623ad1489db32be592625d58e01c368c7568247(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e3ed01afbf4aa2c01303d467dcbf5c5cd3fb267902b917f3c4f5fdd0d83ccdc(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cb84ad0dc27ffdae65e4e739c98ea6a4e7c36340f15c21ae83a2225ff763ba3(
    *,
    answer_recommendation_ai_agent_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIAgent.AnswerRecommendationAIAgentConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    manual_search_ai_agent_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIAgent.ManualSearchAIAgentConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6847cf788b7def362d576a512b579b2a08c25837003298b7c57254d1dfb45112(
    *,
    answer_generation_ai_prompt_id: typing.Optional[builtins.str] = None,
    association_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIAgent.AssociationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    intent_labeling_generation_ai_prompt_id: typing.Optional[builtins.str] = None,
    query_reformulation_ai_prompt_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c351d3e3386a19a82d6920c115ac6f8c911a12da4a117a9c0676a8ff0038fd41(
    *,
    knowledge_base_association_configuration_data: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIAgent.KnowledgeBaseAssociationConfigurationDataProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2df56062b7b8c55a883d0469e63c3aad05d8079bf21171f13f4e68d2f26fea44(
    *,
    association_configuration_data: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIAgent.AssociationConfigurationDataProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    association_id: typing.Optional[builtins.str] = None,
    association_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af25ecdf7592033a618b9a411d145fb2bd7b10ae3e9b0a04a4502e0dee139e27(
    *,
    content_tag_filter: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIAgent.TagFilterProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    max_results: typing.Optional[jsii.Number] = None,
    override_knowledge_base_search_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3346eba3a05ad4b31350bf2c54edbb6063a18cfea8a25ebbab80c402438f039a(
    *,
    answer_generation_ai_prompt_id: typing.Optional[builtins.str] = None,
    association_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIAgent.AssociationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf2bbad68aea63c5546563872782e30b131382ddae5fbabf04602b928494d4d4(
    *,
    and_conditions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIAgent.TagConditionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tag_condition: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIAgent.TagConditionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76535774a57202e416fb208d73c095c91408f65fd8a1b99f6b568fd994b915e9(
    *,
    key: builtins.str,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47961a691b994d09a0537dc7d655a0aab653585a5e8bd78b30c4bc84ec243c19(
    *,
    and_conditions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIAgent.TagConditionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    or_conditions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIAgent.OrConditionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tag_condition: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIAgent.TagConditionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1cda9a6282ec07c28c0ef49efdf8da8f079052d26edd32bbe15324644982756(
    *,
    assistant_id: builtins.str,
    configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIAgent.AIAgentConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    type: builtins.str,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa5a166c3d658d9410f80c3ff44a4aee88b29cb4def5f6c7d811c5b47f5ffb68(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    ai_agent_id: builtins.str,
    assistant_id: builtins.str,
    modified_time_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eec3c0a8aee757b615051ab77f3708fef64acd48758d58f7b8801c7073f3ea55(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1eec2d46406b6deb09ae2fc5f30e9bb5223c8f293091f02f7d13f928906953a1(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df356486e6fdad853cdc4c3aa5d62a5febffd1441d8e82f3a672bf4aef6e809d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3c00eedc618755e116ec4cf13129b9ecab51c03e0aa3285aa6c4eca0e7c9311(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1cbb04d6951221f1cfd98bc4ebed42ba72b9f79a3ef0707bfcea622572f06cd2(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ce55b0c69b9bc58cfcaeadaff04d7986170a5f73af9f6157ba1fe19c79b250e(
    *,
    ai_agent_id: builtins.str,
    assistant_id: builtins.str,
    modified_time_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48a265f7ec519ced4028dd8e69d5a1fe8ef89d36b11d693c968f74c8be6bb9df(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    api_format: builtins.str,
    model_id: builtins.str,
    template_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIPrompt.AIPromptTemplateConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    template_type: builtins.str,
    type: builtins.str,
    assistant_id: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7567e2bb6113fabf7ae624801bcdbbfa2507650c0fcedb4572ac328601553fcc(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c65608208361b5449f96e9e897202e481d956b960bbccf8366c60dac3e4bd70(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6643cec138a765effc7d182e3db5b09b1ddb19205b800c1f517cbed5e73488b5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be2ea2c4f381a43b0574cf9f6fdcace2ba70655e5f3ebd78fd5e8c4541b05982(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5419aa0c5422844ff34f9fc9a194021532fa6ada449722bb2aa4b846530445ba(
    value: typing.Union[_IResolvable_da3f097b, CfnAIPrompt.AIPromptTemplateConfigurationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e4b3aeb8d77c711927acf1f94798cc7b4e483f8fc8bc95ae0b322f2c18a51f0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3f45400801eabea6672075f9e78a389daf48244d79b0b5601339aad9840939b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5634dda4bc6094fc31dbde0ffceab32283f49a381e6e026ed12c76738e89fe5e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4aab971aeb8e18c48f506a9f2350fb427745d11ff1d792a38763843c7c52200b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c8237463d9724c409122f49c9b69b5a1e0f429714ecc37326da2fb2d24ac916(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ebc135e5b323c7d3a33dd614d94d6bb8425982f46dc4aafee23df90fac59a460(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5c009da191a8948caab2f589b801cb2b5b6bd6f17d15c830bfcc3eac735974e(
    *,
    text_full_ai_prompt_edit_template_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIPrompt.TextFullAIPromptEditTemplateConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aab519c6a13d7d17f031944b9ddc67f7d24074f5ba48e4816f1ba2dfd7883ffc(
    *,
    text: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a55de2153828f44950073a28af3416601dc1f09105d3fa9d8f1ec243b3822d3(
    *,
    api_format: builtins.str,
    model_id: builtins.str,
    template_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIPrompt.AIPromptTemplateConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    template_type: builtins.str,
    type: builtins.str,
    assistant_id: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__729db38c828e5e73ae0386aea45298b479e1a069777600fadadd338035a13e5d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    ai_prompt_id: builtins.str,
    assistant_id: builtins.str,
    modified_time_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb551060d0407b951291352d04af15e21651dd34a52774e39a2d2da6e4df3220(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b234db791908c37519c8ae3284494dc43affe3bad0ab4eadab6407ef7ccc7627(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad29e2ee6fad75de44645890c2c623b9ccb35a02f6e75d7ed98fa3b7337272ca(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b6982f0f13d49bf234e47082e4a9783bc461e6dc18d68737a370a3682f93b48(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1f64ffa51639af07e9712d95780a238db8bd368a440a159ead5f0364951dcd4(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39068faf047cdd2f1dce0d86adaff6f71058bba08c161da563b36647959f2add(
    *,
    ai_prompt_id: builtins.str,
    assistant_id: builtins.str,
    modified_time_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8078b7e28a17a68ab6f3d362e7de3af6b6867207690b2b344e35797cd6569746(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    type: builtins.str,
    description: typing.Optional[builtins.str] = None,
    server_side_encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssistant.ServerSideEncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67a0860b53a1867e3124a155db57aa1ab8bbb2d50c48a1553f8766101996d0b8(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a17095196842a083c7a71c961443f89f6d1dd766154e06248d10cdee66b0113(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ded25c09bd072cbcb02cdfdf40580d154663664980378f96c5210edc137dd8c0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c131b16ef6a21690f65d4e643bc0f04ea3e1fa9afd2bbf0e89a9bd4b96032657(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17115c2ceb35036c54e25dfa13fd4465303e5a759aae943761c84163427b74ed(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb8470e364668ea9060baa4a3306507e0ded02773f75cc435d33474d30577d1b(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAssistant.ServerSideEncryptionConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a82c89946835215b7304a7033eacc23c202ee6ae8e17e73d0ba34f1dbaf1416(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa78e1cc313485ba353b8f1dc8b01c69bcdd1c5bcecd204b9778596de1e4a07d(
    *,
    kms_key_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17f6f8491bb7be7dab63c57bf64b65f643c4fece381b02f49002f796c7a8f0f9(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    assistant_id: builtins.str,
    association: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssistantAssociation.AssociationDataProperty, typing.Dict[builtins.str, typing.Any]]],
    association_type: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a96af34ce4ed10cd5d626bf5df7799b86ca3023d4f6b302c0cdb51a0bdd1274(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e84fe37792368fc9821204b49ed0d6e13642f35bcdc7bb2676de0ee949767075(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c72c215a467df1527e01f95d41dc85287728a80fa94729b3ff14b2b1312fb30(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e46eeb6364ccf0b8f92618927437f56df6248417cb401c056b83fe5692feb0f8(
    value: typing.Union[_IResolvable_da3f097b, CfnAssistantAssociation.AssociationDataProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48fcb269f8dde8b147d1a0d7681e40817cb35b599f00a24aff263a84df4cea90(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea3d3cb4fe1048c256fc8719ac3d18f47cb21ef29730dd9d1f53a9304ccd4030(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6ecf0cfb2eb97624a8ec4ab51e16f75cfa1a5397890274252a2621ff5ad378d(
    *,
    knowledge_base_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__419e70156a249f4fa2bea77a71d532fe9a351e3d150b5939dc8455b174375514(
    *,
    assistant_id: builtins.str,
    association: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssistantAssociation.AssociationDataProperty, typing.Dict[builtins.str, typing.Any]]],
    association_type: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2f6978729a0bccb7cc077df26ee5d379812791b9fe7ec0622251ed958562e07(
    *,
    name: builtins.str,
    type: builtins.str,
    description: typing.Optional[builtins.str] = None,
    server_side_encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssistant.ServerSideEncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99512a2eb8a3e47802b889aac668fc94bdc0534ee683313dac712b20006ea6ed(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    knowledge_base_type: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    rendering_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnKnowledgeBase.RenderingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    server_side_encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnKnowledgeBase.ServerSideEncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    source_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnKnowledgeBase.SourceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e12fde615d3c7854b4e97326fea29e89d837485efe274039378606ee08a4be76(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__198b767f5d7e7dce9b330a5c5c43441fed236182c59b06b0be2da034b14ce256(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93bc0b75027c2aaed7afea32df7bbe9ea25daf054d032e869d4b65d3c73427e3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06da4251d33a92a96fd91655710caf394cf4fa6fe728e86b20be47c80f50c450(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8e87e39918fdfb349935e6c5b5b76307ecd838c21583fab217f7d88ca3ea67c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3dbfe6a279891a574d7128da28db41ca74ec109e76fb61b5b9db27b1ee815fba(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnKnowledgeBase.RenderingConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__221e4b62cf601d8c0e6300aceb9f7a7bfe38ac19093345137be6abb3f22756d8(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnKnowledgeBase.ServerSideEncryptionConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ab7292e64b294c529dec00a33cfb2da96ff80581b3e1376c67027a944849691(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnKnowledgeBase.SourceConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b654968450798e9434ae157e80b0efdde965d3d9cf517c41c4fcdcfa66e910f8(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb5af4edc537ecd6b5dab081c90708156852ccef10f7a6228ff445f6dc0e509c(
    *,
    app_integration_arn: builtins.str,
    object_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc0b3350c030b63153dd14a7ab6b7c686549027289e97b41678c46c5c9bce0d1(
    *,
    template_uri: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0cd7e6721b8c282e7e8effcea12ef5d59096c2d9eb9611a2269ac2deff0e697(
    *,
    kms_key_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__169c34939e73e3c8ce81d921898915b159d4e29ad0c3757e50950775728d0aa0(
    *,
    app_integrations: typing.Union[_IResolvable_da3f097b, typing.Union[CfnKnowledgeBase.AppIntegrationsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b2c89f78d66a3c10ed4851c5bc420028f69cc91ddabbe2ac038dd7332ea1edd(
    *,
    knowledge_base_type: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    rendering_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnKnowledgeBase.RenderingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    server_side_encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnKnowledgeBase.ServerSideEncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    source_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnKnowledgeBase.SourceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
