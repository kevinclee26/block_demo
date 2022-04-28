import streamlit as st
import block
import pandas as pd

@st.cache(allow_output_mutation=True)
def setup(): 
    genisus_block=block.Block(0, 0, 0)
    new_chain=block.StockChain([genisus_block])
    return new_chain

st.markdown('# THIS IS THE BLOCKCHAIN DEMO #')

stock_chain=setup()

st.markdown('## Enter Your Transaction Details Below: ##')

buyer_id=st.text_input('Buyer ID')
seller_id=st.text_input('Seller ID')
shares=st.text_input('Shares Transacted')

# add block to chain
if st.button('Add Block'): 
    # get last block
    last_block=stock_chain.chain[-1]
    # instantiate new block with hash of previous block
    new_block=block.Block(shares, buyer_id, seller_id, prev_hash=last_block.hash_block())
    stock_chain.add_block(new_block)
    st.balloons()

ledger_df=pd.DataFrame(stock_chain.chain).astype(str)

st.write(ledger_df)

st.sidebar.markdown('### Block Inspector ###')
block_selected=st.sidebar.selectbox('Select a Block', stock_chain.chain)
if st.sidebar.button('Hash Block'): 
    st.sidebar.write(block_selected.hash_block())