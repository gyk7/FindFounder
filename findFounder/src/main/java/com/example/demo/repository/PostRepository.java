package com.example.demo.repository;



import java.util.List;

import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import com.example.demo.model.entity.Customer;
import com.example.demo.model.entity.Post;


@Repository
public interface PostRepository extends JpaRepository<Post, Integer>{
//	List<Post> findAll(int postId);
	
//	List<Post> findAllByPostTitleContaining(String keyword);
	
//	List<Post> findAllByCustomer(Customer customer);
	
	@Query("select p from Post p join  p.customer order by p.postId DESC")
    List<Post> findAllFetchJoin();
	
	@Query("select p from Post p join fetch p.customer where p.postTitle like %:keyword% order by p.postId DESC")
    List<Post> findAllByPostTitleContainingFetchJoin(@Param("keyword") String keyword);
	
	@Query("select p from Post p join fetch p.customer where p.customer = :customer order by p.postId DESC")
    List<Post> findAllByPostCustomerFetchJoin(@Param("customer") Customer customer);
	
	void deleteAllByCustomer_CusCode(int cusCode);

	
	
}
