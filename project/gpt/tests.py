#from django.test import TestCase

# Create your tests here.

import os
import openai
import chromadb

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores.chroma import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.text_splitter import CharacterTextSplitter

import logging
from django.conf import settings

avoid_embedding = "off"

def make_show_business():
    
    #For spliting a text
    #loader = PyPDFLoader(f"{pdf_path}")
    #MinerLoaderめちゃ重くない？？
    #loader = PDFMinerLoader(f"{pdf_path}")
    #text_spliter = CharacterTextSplitter(chunk_size=400)

    discription = "\
    #company_number:1\
    FutureTech Innovationsについて\
    FutureTech Innovationsは、未来を切り拓くイノベーション企業です。私たちは、最新のテクノロジーとクリエイティブなアイディアを組み合わせ、世界中のビジネスと社会にポジティブな変革をもたらすことを使命としています。グローバルな視点と卓越した専門知識を持つチームが、未来の課題に対処し、新たな可能性を切り開いています。\
    \
    #求人情報\
    ##offer_id:1\
    #company_number:1\
    AIシステムエンジニア\
    職務内容: 機械学習アルゴリズムの開発および実装\
    応募資格: コンピュータサイエンスの学位と豊富なAI開発経験\
    \
    ##offer_id:2\
    #company_number:1\
    サイバーセキュリティアナリスト\
    職務内容: システムの脆弱性の分析とセキュリティ対策の実装\
    応募資格: サイバーセキュリティの専門知識と実務経験\
    \
    ##offer_id:3\
    #company_number:1\
    クリエイティブデザイナー\
    職務内容: グラフィックデザインおよびウェブデザインの制作\
    応募資格: クリエイティブな発想力とデザインスキル\
    \
    ##offer_id:4\
    #company_number:1\
    ブロックチェーン開発者\
    職務内容: 分散型アプリケーションの開発とスマートコントラクトの実装\
    応募資格: ブロックチェーン技術の深い理解と開発経験\
    \
    ##offer_id:5\
    #company_number:1\
    持続可能性コンサルタント\
    職務内容: 環境に配慮したビジネス戦略の提案と実施\
    応募資格: 持続可能性領域でのコンサルティング経験\
    \
    ##offer_id:6\
    #company_number:1\
    宇宙開発プロジェクトマネージャー\
    職務内容: 宇宙探査プロジェクトの計画と実行\
    応募資格: 宇宙工学または関連分野の学位とプロジェクトマネージメントの経験\
    \
    ##offer_id:7\
    #company_number:1\
    データサイエンティスト\
    職務内容: 大量のデータから優れた洞察を得るための分析\
    応募資格: 統計学や機械学習の専門知識とデータ解析の経験\
    \
    ##offer_id:8\
    #company_number:1\
    ロボット工学エンジニア\
    職務内容: ロボットの設計と制御システムの開発\
    応募資格: ロボット工学または制御工学の学位と関連する技術スキル\
    \
    ##offer_id:9\
    テクニカルライター\
    #company_number:1\
    職務内容: 技術的なドキュメントやマニュアルの作成\
    応募資格: 技術分野での執筆経験とコミュニケーション能力\
    \
    ##offer_id:10\
    #company_number:1\
    量子コンピューティング研究者\
    職務内容: 量子コンピューティング技術の研究と実装\
    応募資格: 量子コンピューティングの専門知識と研究経験\
    興味をお持ちいただけた方は、履歴書と職務経歴書を添えて、recruitment@futuretechinnovations.com までご応募ください。"
    
    text_splitter = CharacterTextSplitter(
    separator = "##",
    chunk_size = 1000,
    chunk_overlap  = 200,
    length_function = len,
    is_separator_regex = False,
    )
    
    pages = text_splitter.create_documents([discription])

    #OpenAI's apikey is already set to load from environment variables.
    openai.api_key = "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"
    os.environ["OPENAI_API_KEY"] = openai.api_key
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    
    openai_ef = OpenAIEmbeddings()
    persist_path = "/Users/kazukikuriyama/hackathon/login-func/first-repo/project" + "/Chroma"
    
    """
    if (avoid_embedding != "on"):
        logging.debug("debug off")
        #Note that if a collection with the same collection name already exists, a new one will be created separately.
        collection = Chroma(collection_name="langchain_test", embedding_function=openai_ef, persist_directory=persist_path)
        vectorstore = collection.from_documents(pages,embedding=openai_ef, persist_directory=persist_path)
    else:
        client = chromadb.PersistentClient(path=persist_path)
        vectorstore = Chroma(collection_name="langchain_test", client=client, embedding_function=openai_ef)
    
    pdf_qa = ConversationalRetrievalChain.from_llm(llm, vectorstore.as_retriever(), return_source_documents=True, verbose=True)

    query = "##以下の人物にとってふさわしい案件とその理由を教えてください。offer_idも返答してください。\
    応募者: 田中 明子\
    1. AIシステムエンジニア\
    学歴:\
    \
    東京大学　工学部　情報工学科　卒業\
    経歴:\
    \
    XYZテクノロジーズ株式会社　AI開発エンジニア（3年間）\
    機械学習アルゴリズムの開発と実装に従事\
    顧客のニーズに合わせたカスタマイズソリューションの提供\
    スキル:\
    \
    Python, TensorFlow, PyTorchによる開発経験\
    深層学習モデルの設計およびトレーニング\
    自然言語処理（NLP）における豊富な知識\
    ポートフォリオ:\
    \
    GitHub プロフィール\
    開発した機械学習モデルやプロジェクトのソースコード"
    chat_history = []

    result = pdf_qa({"question": query, "chat_history": chat_history})
    """
    
    #return result["answer"]
    return pages

res = make_show_business()

print(res)