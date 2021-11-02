package com.example.fdutext_2;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.content.Intent;
import android.os.Bundle;
import android.text.Editable;
import android.text.TextWatcher;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.EditText;
import android.widget.Filter;
import android.widget.Filterable;
import android.widget.TextView;

import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {
    private EditText et_search;
    private RecyclerView mRecycleView;
    private SearchAdapter mSearchAdapter = new SearchAdapter();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mRecycleView = findViewById(R.id.rv);
        mRecycleView.setLayoutManager(new LinearLayoutManager(this));
        mRecycleView.setAdapter(mSearchAdapter);

        List<String> items = new ArrayList<>();
        for(int i = 0;i<100;i++)
        {
            items.add("这是第" + i + "行");
        }
        mSearchAdapter.notifyItems(items);



        et_search = findViewById(R.id.edit_query);
        setListeners();
    }
    private void setListeners(){
        et_search.addTextChangedListener(new TextWatcher(){
            public void beforeTextChanged(CharSequence s, int start, int count, int after){

            }

            public void onTextChanged(CharSequence s, int start, int before, int count){
               mSearchAdapter.getFilter().filter(s.toString());
            }

            public void afterTextChanged(Editable s){

            }
        });
    }
}







class TextViewHolder extends RecyclerView.ViewHolder implements View.OnClickListener{

    private TextView mTextView;

    public TextViewHolder(@NonNull View itemView) {
        super(itemView);
        mTextView = itemView.findViewById(R.id.rv_text);
        itemView.setOnClickListener(this);
    }
    public void bind(String text){mTextView.setText(text);}

    @Override
    public void onClick(View v) {
        Intent intent = new Intent(v.getContext(),MainActivity.class);
        intent.putExtra("itemId",mTextView.getText().toString());
        v.getContext().startActivity(intent);
    }
}








class SearchAdapter extends RecyclerView.Adapter<TextViewHolder> implements Filterable {

    private List<String>mItems = new ArrayList<>();
    private List<String>filterItems = new ArrayList<>();

    @NonNull
    @Override
    public TextViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        return new TextViewHolder(LayoutInflater.from(parent.getContext())
        .inflate(R.layout.item_list,parent, false));
    }

    @Override
    public void onBindViewHolder(@NonNull TextViewHolder holder, int position) {
        holder.bind(filterItems.get(position));
    }

    @Override
    public int getItemCount() {
        return filterItems.size();
    }

    public void notifyItems(@NonNull List<String> items){
        this.mItems = items;
        this.filterItems.clear();
        this.filterItems.addAll(items);
        notifyDataSetChanged();
    }

    @Override
    public Filter getFilter() {
        return new Filter() {
            @Override
            protected FilterResults performFiltering(CharSequence constraint) {
                String charString = constraint.toString();
                if (charString.isEmpty()) {
                    filterItems = mItems;
                } else {
                    List<String> filtered = new ArrayList<>();
                    for (String item : mItems) {
                        if (item.contains(charString)) {
                            filtered.add(item);
                        }
                    }
                    filterItems = filtered;
                }
                FilterResults filterResults = new FilterResults();
                filterResults.values = filterItems;
                return filterResults;
            }

            @Override
            protected void publishResults(CharSequence constraint, FilterResults results) {
                filterItems = (ArrayList<String>) results.values;
                notifyDataSetChanged();
            }
        };
    }
}








class ItemActivity extends AppCompatActivity {
    private TextView textView;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.item_ac);

        textView = findViewById(R.id.tv_item);
        textView.setText("you just clicked " +
                getIntent().getStringExtra("itemId"));
    }
}

