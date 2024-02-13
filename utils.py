from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain.prompts import PromptTemplate
from langchain_community.document_loaders import AsyncHtmlLoader
from langchain_community.document_transformers import Html2TextTransformer

from langchain.prompts.pipeline import PipelinePromptTemplate
from langchain.prompts.prompt import PromptTemplate


def get_content_from_url(urls):
    urls_regulations = urls
    loader = AsyncHtmlLoader(urls_regulations)
    docs_regulations = loader.load()

    html2text = Html2TextTransformer()
    docs_regulations = html2text.transform_documents(docs_regulations)
    return [docs.page_content for docs in docs_regulations]



def create_prompt(compliance_authority, regulations_set, input_content):
    # create prompts
    full_template = """{introduction}

        {regulations}
        
        {input_content}"""

    full_prompt = PromptTemplate.from_template(full_template)

    introduction_template = """You are impersonating strict {compliance_authority}."""
    introduction_prompt = PromptTemplate.from_template(introduction_template)

    # consider few shot examples.
    regulations_template = """below are set of regulations to be followed:

    {regulations}"""
    regulations_template = PromptTemplate.from_template(regulations_template)


    input_content_template = """Now, check if below input follow all the above regulations. Provide all regulations which are not followed in below input.

    {input}
    A:"""
    input_content_template = PromptTemplate.from_template(input_content_template)


    input_prompts = [
        ("introduction", introduction_prompt),
        ("regulations", regulations_template),
        ("input_content", input_content_template),
    ]
    pipeline_prompt = PipelinePromptTemplate(
        final_prompt=full_prompt, pipeline_prompts=input_prompts
    )

    #print(pipeline_prompt.input_variables)

    template = pipeline_prompt.format(
            compliance_authority=compliance_authority,
            regulations=regulations_set,
            input=input_content,
        )
    # print(template)
    return template

